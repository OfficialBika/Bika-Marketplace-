export const marketplaceConfig = {
  characterLabel: process.env.NEXT_PUBLIC_CHARACTER_NAME?.trim() || 'Bika Characters',
  nftLabel: process.env.NEXT_PUBLIC_NFT_NAME?.trim() || 'BIKA',
  coinLabel: process.env.NEXT_PUBLIC_COIN_NAME?.trim() || 'BKC',
  maxActiveAuctions: Number(process.env.NEXT_PUBLIC_MAX_AUCTIONS || 3),
  rarity: ['CrossVerse','Divine','Mystical','Cataphract','Supreme']
};
