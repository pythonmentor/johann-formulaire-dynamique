/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "src/**/*.{js,css,scss,html}",
    "../exemple//**/*.{js,css,scss,html,py}",
    "../.venv/**/crispy_tailwind/**/*.{js,css,scss,html}"
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require('daisyui'),
  ],
}

