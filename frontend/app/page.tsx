"use client";

import Link from "next/link";
import CharacterCatcher from '@/components/CharacterCatcher';

const menus = [
 {name:'Rewards',path:'/rewards'},
 {name:'Wallet',path:'/wallet'},
 {name:'Gate',path:'/gate'},
 {name:'Trade',path:'/trade'},
 {name:'Cleaning',path:'/cleaning'},
 {name:'Purchase',path:'/purchase'},
 {name:'NFT',path:'/nft'},
 {name:'Auction',path:'/auction'}
];

const nfts=[
 {id:'supreme-cell',name:'Cell'},
 {id:'nahida-prime',name:'Nahida'},
 {id:'changli-flame',name:'Changli'},
 {id:'keqing-shadow',name:'Keqing'}
];

export default function Home(){
 return (
  <main className="dashboard">
   <aside className="sidebar">
    <h1>BIKA</h1>
    <h2>MARKETPLACE</h2>
    <p>Advanced NFT & Characters Hub</p>
   </aside>

   <section className="content">
    <header className="profile">
     <div><h2>Official Bika</h2><p>BKC Character Trading Hub</p></div>
     <strong>🪙 68.02 BKC</strong>
    </header>

    <section className="hero">WELCOME<br/><small>GO BIKA MARKETPLACE</small></section>

    <div className="menu-grid">
     {menus.map(m=>(
      <Link key={m.name} href={m.path} className="card">{m.name}</Link>
     ))}
    </div>

    <h2 className="title">🔥 Supreme Character Showcase</h2>
    <CharacterCatcher />

    <h2 className="title">Bika Characters</h2>
    <div className="nft-grid">
     {nfts.map(n=>(
      <article className="nft" key={n.id}>
       <div className="image">NFT</div>
       <b>{n.name}</b>
       <p>Rare Character • Mystical</p>
       <Link href={`/character/${n.id}`} className="purchase-btn">VIEW DETAIL</Link>
      </article>
     ))}
    </div>
   </section>
  </main>
 );
}
