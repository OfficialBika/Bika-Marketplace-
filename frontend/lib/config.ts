export const appConfig = {
  rarity: process.env.NEXT_PUBLIC_SHOW_RARITY || "Supreme",
  rotation: Number(process.env.NEXT_PUBLIC_CHARACTER_ROTATION || 5000)
};
