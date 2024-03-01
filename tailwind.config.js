/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require("rippleui")
  ],
  rippleui: {
		themes: [
			{
				themeName: "light",
				colorScheme: "light",
				colors: {
					primary: "#573242",
					backgroundPrimary: "#1a1a1a",
				},
			},
			{
				themeName: "dark",
				colorScheme: "dark",
				colors: {
					primary: "#252525",
          			secondary: "#FFFFFF",
          			TextTertiary: "#252525",
				},
			},
		],
	},
	screens: {
		'phone-s': '320px',
		'phone-m': '375px',
		'phone-l': '425px',
		'tablet': '768px',
		'laptop': '1024px',
		'laptop-l': '1440px',
		'4K': '2560px',
	  },
}