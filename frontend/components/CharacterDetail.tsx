import { nftDisplayName, coinDisplayName } from '@/lib/names';

export default function CharacterDetail({name,rarity,price}:{name:string;rarity:string;price:number}){
 return <div className="rounded-3xl border border-white/20 bg-white/5 p-6">
  <h2 className="text-2xl font-bold">{nftDisplayName}</h2>
  <p>{name}</p>
  <p>Rarity: {rarity}</p>
  <p>{price} {coinDisplayName}</p>
 </div>
}
