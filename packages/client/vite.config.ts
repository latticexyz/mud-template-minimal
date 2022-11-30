import { defineConfig } from "vite";
export default defineConfig({
  server: {
    port: 3000,
    fs: {
      strict: false,
    },
  },
  optimizeDeps: {
    esbuildOptions: {
      target: "es2020",
    },
    exclude: ["@latticexyz/network"],
  },
});
