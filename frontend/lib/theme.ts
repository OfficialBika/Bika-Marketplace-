export type MarketplaceTheme = 'neon' | 'redblue';

export const marketplaceTheme: MarketplaceTheme =
  (process.env.NEXT_PUBLIC_THEME as MarketplaceTheme) || 'neon';

export const themes = {
  neon: {
    name: 'Neon',
    background: 'from-purple-950 via-black to-blue-950',
    accent: 'pink-cyan'
  },
  redblue: {
    name: 'RedBlue',
    background: 'from-red-950 via-black to-blue-950',
    accent: 'red-blue'
  }
};
