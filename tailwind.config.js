module.exports = {
  purge: [],
  theme: {
    fontFamily: {
        display: ['Open Sans', 'sans-serif'],
        body: ['Comfortaa', 'cursive'],
      },
      colors: {
        background: {
            'primary' : 'var(--bg-background-primary)',
            'secondary' : 'var(--bg-background-secondary)',
            'ternary' : 'var(--bg-background-ternary)',
            'fourth' : 'var(--bg-background-fourth)',
        },
        copy: {
            'primary' : 'var(--color-primary)',
            'secondary' : 'var(--color-secondary)',
            'ternary' : 'var(--color-ternary)',
            'fourth' : 'var(--color-fourth)',
        }
      },
    extend: {
        screens: {
            'dark-mode': { raw: '(prefers-color-scheme: dark)' }
        },
    },
  },
  variants: {},
  plugins: [],
}
