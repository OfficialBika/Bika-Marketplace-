export const themes = {
  neon: {
    background: 'from-purple-950 via-black to-blue-950',
    primary: 'pink',
  },
  redblue: {
    background: 'from-red-950 via-black to-blue-950',
    primary: 'cyan',
  },
};

export type ThemeName = keyof typeof themes;
