export default function DashboardStats({stats}:{stats:{title:string,value:string}[]}){
 return <div className="grid gap-4 md:grid-cols-3">
 {stats.map((s)=>(
  <div key={s.title} className="rounded-3xl border border-white/20 bg-white/5 p-5">
   <div>{s.title}</div>
   <div className="text-2xl font-bold">{s.value}</div>
  </div>
 ))}
 </div>
}
