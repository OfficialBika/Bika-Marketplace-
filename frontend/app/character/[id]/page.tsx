export default function Page({params}:{params:{id:string}}){
 return <main className="home"><h1>Character Detail</h1><p>ID: {params.id}</p></main>
}
