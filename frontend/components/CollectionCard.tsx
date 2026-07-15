export default function CollectionCard({name='Collection',count=0}:{name?:string;count?:number}){
 return <div className="rounded-2xl border p-5">
  <h3 className="font-bold">{name}</h3>
  <p>{count} items</p>
 </div>;
}
