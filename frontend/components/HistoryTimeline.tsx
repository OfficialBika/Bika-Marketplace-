export default function HistoryTimeline({items}:{items:string[]}){
 return <div className="space-y-3">
  {items.map((item,index)=>(
   <div key={index} className="rounded-xl border border-white/20 bg-white/5 p-4">
    {item}
   </div>
  ))}
 </div>
}
