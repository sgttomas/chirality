/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  transpilePackages: ['@chirality/runtime-contracts'],
  serverExternalPackages: ['@earendil-works/pi-coding-agent']
};

export default nextConfig;
