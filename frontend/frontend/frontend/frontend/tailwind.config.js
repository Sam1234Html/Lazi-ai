/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        'deep-brown': '#3D2B1F',
        'warm-brown': '#8B5A2B',
        'near-black': '#2A2A2A',
        'paper-bg': '#F5EFE6',
      },
    },
  },
  plugins: [],
};
