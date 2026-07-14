import { coinDisplayName } from '@/lib/names';

export default function WalletCard({balance}:{balance:number}){
 return <div className="rounded-3xl border border-white/20 bg-white/5 p-6">
   <div className="text-sm opacity-70">Balance</div>
   <div className="text-3xl font-bold">{balance} {coinDisplayName}</div>
 </div>
}
