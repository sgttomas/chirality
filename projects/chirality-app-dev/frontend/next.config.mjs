/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  transpilePackages: ['@chirality/harness-contract'],
  experimental: {
    serverComponentsExternalPackages: ['@earendil-works/pi-coding-agent']
  }
};

export default nextConfig;
