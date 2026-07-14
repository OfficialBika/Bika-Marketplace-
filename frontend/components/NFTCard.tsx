import { nftDisplayName } from '@/lib/names';

export default function NFTCard({name, rarity, price}: {name:string; rarity:string; price:string}){
 return <div className="rounded-3xl border border-white/20 bg-white/5 p-5 backdrop-blur">
  <div className="text-xl font-bold">{nftDisplayName}</div>
  <div>{name}</div>
  <div className="text-sm">{rarity}</div>
  <div className="mt-3">{price}</div>
 </div>
}
