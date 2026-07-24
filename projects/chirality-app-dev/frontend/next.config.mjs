/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  transpilePackages: ['@chirality/harness-contract'],
  serverExternalPackages: ['@earendil-works/pi-coding-agent']
};

export default nextConfig;
