export default function Marketplace(){
 const items=['Cell','Nahida','Changli','Keqing','Bika Dragon'];
 return <main className="home"><h1>NFT Marketplace</h1><p>Buy, sell and trade Bika Characters</p><div className="nft-grid">{items.map(x=><article className="nft" key={x}><div className="image">{x}</div><h3>{x}</h3><p>Rare • Legendary Character</p><button>BUY NOW</button></article>)}</div></main>
}
