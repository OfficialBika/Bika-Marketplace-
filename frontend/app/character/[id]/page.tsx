export default async function CharacterPage({params}:{params:{id:string}}){
  return (
    <main className="home">
      <h1>Character Detail</h1>
      <p>ID: {params.id}</p>
      <section className="nft">
        <h2>Supreme Character</h2>
        <p>Ready for marketplace purchase and trade.</p>
        <button className="purchase-btn">BUY WITH BKC</button>
      </section>
    </main>
  );
}
