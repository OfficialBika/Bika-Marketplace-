export default function EmptyState({title}:{title:string}){
 return <div className="rounded-3xl border border-white/20 bg-white/5 p-8 text-center">
   <div className="text-xl font-bold">{title}</div>
   <div className="mt-2 opacity-70">No data available</div>
 </div>
}
