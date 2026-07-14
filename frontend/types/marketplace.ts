export interface CharacterCard {
  id: string;
  name: string;
  image: string;
  rarity: string;
  catches: number;
  seller: string;
}

export interface AuctionHistory {
  id: string;
  characterId: string;
  action: 'BID' | 'WON' | 'SOLD';
  amount: number;
  user: string;
  createdAt: Date;
}

export interface SpinResult {
  reward: string;
  amount: number;
  rarity?: string;
}
