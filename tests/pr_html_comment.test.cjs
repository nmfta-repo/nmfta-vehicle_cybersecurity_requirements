const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const test = require('node:test');

const workflow = fs.readFileSync(path.join(__dirname, '../.github/workflows/pr-html-comment.yml'), 'utf8');
const script = workflow.split('          script: |\n')[1]
  .split('\n').map(line => line.startsWith('            ') ? line.slice(12) : line).join('\n');
const execute = new (Object.getPrototypeOf(async function () {}).constructor)('github', 'context', 'core', script);

const run = { id: 12, head_sha: 'abc123', head_branch: 'feature' };
const pull = { number: 58, state: 'open', base: { ref: 'main' }, head: { ref: 'feature', sha: 'abc123' } };

async function invoke({ pulls = [pull], artifacts = [{ id: 42, name: 'html-pages', expired: false, created_at: '2026-01-01' }], comments = [] } = {}) {
  const calls = [];
  const failures = [];
  const methods = {
    pulls: async () => pulls,
    artifacts: async () => artifacts,
    comments: async () => comments,
    create: async params => calls.push(params),
  };
  const github = {
    rest: {
      repos: { listPullRequestsAssociatedWithCommit: methods.pulls },
      actions: { listWorkflowRunArtifacts: methods.artifacts },
      issues: { listComments: methods.comments, createComment: methods.create },
    },
    paginate: (method, params) => method(params),
  };
  const context = {
    payload: { workflow_run: run },
    repo: { owner: 'org', repo: 'repo' },
    serverUrl: 'https://github.com',
  };
  await execute(github, context, { info: () => {}, setFailed: message => failures.push(message) });
  return { calls, failures };
}

test('posts the current artifact to the matching PR', async () => {
  const { calls, failures } = await invoke();
  assert.deepEqual(failures, []);
  assert.equal(calls.length, 1);
  assert.equal(calls[0].issue_number, 58);
  assert.match(calls[0].body, /commit `abc123`/);
  assert.match(calls[0].body, /https:\/\/github\.com\/org\/repo\/actions\/runs\/12\/artifacts\/42/);
});

test('ignores stale, closed, and unrelated pull requests', async () => {
  const pulls = [
    { ...pull, head: { ...pull.head, sha: 'newer' } },
    { ...pull, state: 'closed' },
    { ...pull, base: { ref: 'other' } },
    { ...pull, head: { ...pull.head, ref: 'other' } },
  ];
  assert.equal((await invoke({ pulls })).calls.length, 0);
});

test('fails explicitly when the HTML artifact is unavailable', async () => {
  const { calls, failures } = await invoke({ artifacts: [{ id: 42, name: 'html-pages', expired: true }] });
  assert.equal(calls.length, 0);
  assert.equal(failures.length, 1);
});

test('does not duplicate bot comments but posts a new artifact from a rerun', async () => {
  const comments = [{ user: { login: 'github-actions[bot]' }, body: '<!-- pr-html-artifact: 42 -->' }];
  assert.equal((await invoke({ comments })).calls.length, 0);
  const artifacts = [
    { id: 42, name: 'html-pages', expired: false, created_at: '2026-01-01' },
    { id: 40, name: 'html-pages', expired: false, created_at: '2026-01-02' },
  ];
  const { calls } = await invoke({ artifacts, comments });
  assert.equal(calls.length, 1);
  assert.match(calls[0].body, /artifacts\/40/);
});

test('does not trust another user to suppress the bot comment', async () => {
  const comments = [{ user: { login: 'someone' }, body: '<!-- pr-html-artifact: 42 -->' }];
  assert.equal((await invoke({ comments })).calls.length, 1);
});
