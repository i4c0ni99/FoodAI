/** @type {import('tailwindcss').Config} */
export default {
  daisyui: {
    themes: [
      {
        dark: {
          primary: "#009af8",
          "primary-content": "#000915",
          secondary: "#007796",
          "secondary-content": "#d3e3ea",
          accent: "#00ba99",
          "accent-content": "#000d08",
          neutral: "#0f0f14",
          "neutral-content": "#c8c8ca",
          "base-100": "#202127",
          "base-200": "#1a1b20",
          "base-300": "#15161a",
          "base-content": "#cdcdcf",
          info: "#00e1ff",
          "info-content": "#001216",
          success: "#7fa200",
          "success-content": "#060a00",
          warning: "#8d6100",
          "warning-content": "#e8ded0",
          error: "#ec0042",
          "error-content": "#130001",
        },
        light: {
          primary: "#0058ff",
          "primary-content": "#cee1ff",
          secondary: "#f7ab00",
          "secondary-content": "#150b00",
          accent: "#0093ff",
          "accent-content": "#000816",
          neutral: "#060d07",
          "neutral-content": "#c6c8c6",
          "base-100": "#c6c8c6",
          "base-200": "#c6c8c6",
          "base-300": "#bebeb2",
          "base-content": "#161614",
          info: "#4092ff",
          "info-content": "#010816",
          success: "#30b31f",
          "success-content": "#010c00",
          warning: "#ff9f00",
          "warning-content": "#160900",
          error: "#ec0042",
          "error-content": "#130001",
        },
      },
    ],
  },
  content: ["./index.html", "./src/**/*.{js,jsx,ts,tsx}"],
  theme: {
    extend: {},
  },
  plugins: [
    require("daisyui"),
    function ({ addUtilities }) {
      const newUtilities = {
        ".scrollbar-hide": {
          /* Hide scrollbar for Chrome, Safari and Opera */
          "&::-webkit-scrollbar": {
            display: "none",
          },
          /* Hide scrollbar for IE, Edge and Firefox */
          "-ms-overflow-style": "none" /* IE and Edge */,
          "scrollbar-width": "none" /* Firefox */,
        },
      };
      addUtilities(newUtilities);
    },
  ],
};
