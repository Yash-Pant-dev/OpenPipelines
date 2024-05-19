import type { Config } from 'tailwindcss'
const defaultTheme = require('tailwindcss/defaultTheme')

export default {
  content: ['./app/**/*.{js,jsx,ts,tsx}'],
  theme: {
    extend: {
      colors: {
        blue: "#6689A1",
        grey: "#222831",
        lgrey: "#31363F",
        pink: "#EF798A",
        beige: "#DEDBD2",
        white: "#EEEEEE",
      },
      fontFamily: {
        'sans': ['kulim', ...defaultTheme.fontFamily.sans]
      }
    },
  },
  plugins: [],
} satisfies Config