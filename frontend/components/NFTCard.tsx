import { nftDisplayName } from '@/lib/names';

type Props={name:string; rarity:string; price:string};

export default function NFTCard({name, rarity, price}: Props){
 return <div className="rounded-3xl border border-white/20 bg-white/5 p-5 backdrop-blur">
   <div className="text-xl font-bold">{nftDisplayName}</div>
   <div>{name}</div>
   <div className="text-sm">{rarity}</div>
   <div className="mt-3">{price}</div>
  </div>;
}
