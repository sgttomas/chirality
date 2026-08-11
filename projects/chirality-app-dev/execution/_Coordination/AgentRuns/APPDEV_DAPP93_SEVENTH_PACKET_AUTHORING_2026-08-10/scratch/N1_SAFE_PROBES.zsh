#!/bin/zsh
set -eu
OUTPUT=/Users/ryan/.codex/worktrees/55d3/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP93_SEVENTH_PACKET_AUTHORING_2026-08-10/scratch/N1_SAFE_PROBE_OUTPUT.txt
export PATH=/Users/ryan/.local/share/mise/installs/node/24.18.0/bin:/usr/bin:/bin:/usr/sbin:/sbin
{
  /usr/bin/printf 'N1_SAFE_PROBES_BEGIN\n'
  umask 077
  /usr/bin/printf 'umask='
  umask
  PROBE_ASSIGN=assignment_ok
  export PROBE_ASSIGN
  /bin/test "$PROBE_ASSIGN" = assignment_ok
  cd /private/tmp
  /usr/bin/printf 'cd=%s\n' "$PWD"
  /usr/bin/printf 'redirection_probe\n' >&2
  /usr/bin/printf 'pipeline_probe\n' | /usr/bin/tr -d '\n'
  /usr/bin/printf '\n'
  /bin/test -x /bin/zsh && /usr/bin/printf 'and_probe=ok\n'
  /bin/test 1 -eq 0 || /usr/bin/printf 'or_probe=ok\n'
  if /bin/test -x /bin/zsh; then
    /usr/bin/printf 'if_probe=ok\n'
  fi
  {
    /usr/bin/printf 'brace_probe=ok\n'
  }
  records=(
    '/bin/zsh|528da649cc69510bd3c0bc565298cb602076b74a8ac3f18e793211b2a3c725e8'
    '/usr/bin/printf|f2a76beee50f16a1193244519ecfad592b3af0623276b41c088c0ef8650c05f7'
    '/bin/test|ef72d7615d6f7badb794fbc1f1289b47166a85add6d39d1be3a4f51bcc601640'
    '/bin/mkdir|eb3b48e064031c5491bcb9a99bbf44753c9ee074d10c69d114cb4cbc236ca02c'
    '/usr/bin/sw_vers|a5879fe2c946cbdfb74e3f614d89786031e62e85002ffab7d4047859bbcedd95'
    '/usr/bin/uname|fdd05a10dfc0901947dfe8acd4ad14dae3d7c3efb4701a46ce6b7cb8bffeb5d7'
    '/usr/bin/shasum|0812595f981a26f813d98dc380af14d4af427626c9339eda29eb849ae13de1e3'
    '/bin/cp|48f8e2964a1866e3e734f5dbdd0949ee2f30a881540f8925d480407d1be0f3cc'
    '/Users/ryan/.local/share/mise/installs/node/24.18.0/bin/node|ee6fb0e015284d83a91e8ec5213f43a157f8a392b58555301682892ba928c04a'
    '/Users/ryan/.local/share/mise/installs/node/24.18.0/bin/npm|a74679065974f6fd0a02f7ea8d4690d7bccd6437981924201ed37fc010112e22'
    '/usr/bin/plutil|0814b3dadf0baf367c35c32720cdd3ea76e81ee8de6bd49e06c4ca5855b53132'
    '/usr/bin/find|05aa84ee15d95122cfa3de6a132ace019eb78b27da57534b5d555719c8380f7b'
    '/usr/bin/readlink|a3119dde345aa860c2f2e293ecd5f9f3db450d2570343e3319838ac154617b65'
    '/usr/bin/security|2b5c0eae2ee36c5400309edc44635b07e08dc7d9e3fac26c1fa7612a3493ddc7'
    '/usr/bin/env|6e8b85a2efe5bf44ad11302f2b7b7e8c6b2f2c94f9bf117f5d4654b79bf85271'
    '/bin/ps|a1d8c4a0a96fb6159f09d8f520f54df829db5f2eae9b9f3448e18f0bee61115c'
    '/usr/bin/tr|4e1228488279bbd6dc171c608f2402dd8a3b89dbe45bac13f8bfd8f1bb995b7a'
    '/bin/date|28f40376c23f2d4f8bd58eb27c9aa86c25a51fe949f12dab1bc0254f906aa9f6'
    '/usr/bin/xcrun|4bc0cc7099775fbe35c653ceb09e0e393d2e5ada024db872e0eb8c43500b4dc6'
    '/usr/bin/tee|d284dd54c2e98bd7da539085105bf50a5455eb467c5aaf382413bc0b9b02a226'
    '/usr/bin/awk|3868b14602a4851218210ae1b08732fbdee703ac2c1e2d1898272b42fd33151a'
    '/bin/kill|08fab82eded4aad982575622b90b2c8c6058b241432f66caeaed212347b44160'
    '/usr/bin/cmp|bf0111a82ee28deeb99a83eaee6f0829a743e09dcf8193ebd49b4c4190ad2457'
    '/usr/bin/sort|a61f82d2598a7a5b9cc273e2426b8c19c532eb72963f34dc97c9cd3d1210486f'
    '/usr/bin/xargs|93233b976e06509a1eadd41f7ee21df44b607290b906c12a2ceba3027395e354'
    '/usr/bin/ditto|9c9c5950fe43f23e1a16ed25a0a7c447878710c160fdb9bcfb931d161b716d04'
    '/bin/rm|c12e91a60bbc9da47579b3d78275bd2e08e694833b030b41c7bcdb64f88123e7'
    '/usr/bin/git|44a68ddc1983d6cff3fd35ba3f9ba5f82004216f1dcde69892b3d1b06e408698'
    '/bin/sleep|b675bfecd394b9708eec132b91cecaa5def4b245291d5bf8bdfe531ea0451bde'
  )
  for record in $records; do
    path=${record%%|*}
    expected=${record#*|}
    /bin/test -x "$path"
    /usr/bin/printf 'expected %s  %s\n' "$expected" "$path"
    /usr/bin/shasum -a 256 "$path"
  done
  /bin/test -x /bin/zsh &
  probe_pid=$!
  wait $probe_pid
  /usr/bin/printf 'background_wait_probe=ok\n'
  /usr/bin/readlink /var
  /usr/bin/sort -z /dev/null
  /usr/bin/find /private/tmp -maxdepth 0 -print0
  /usr/bin/printf '\n'
  /usr/bin/xargs -0 /usr/bin/printf </dev/null
  /usr/bin/xcrun lldb --version
  /usr/bin/git --version
  /Users/ryan/.local/share/mise/installs/node/24.18.0/bin/node --version
  /Users/ryan/.local/share/mise/installs/node/24.18.0/bin/npm --version
  /usr/bin/printf 'N1_SAFE_PROBES_COMPLETE\n'
} >"$OUTPUT" 2>&1
