const menus = [
  'Rewards','Wallet','Gate','Trade','Cleaning','Purchase','NFT','Auction'
];

const nfts = ['Cell','Nahida','Changli','Keqing'];

import CharacterCatcher from '@/components/CharacterCatcher';

export default function Home() {
  return (
    <main className="dashboard">
      <aside className="sidebar">
        <h1>BIKA</h1>
        <h2>MARKETPLACE</h2>
        <p>Advanced NFT & Characters Hub</p>
        <ul>
          <li>NFT Marketplace</li><li>Spin Wheel</li><li>Auction System</li>
          <li>Wallet & Transactions</li><li>Trade System</li>
        </ul>
      </aside>

      <section className="content">
        <header className="profile">
          <div><h2>Official Bika</h2><p>BKC Character Trading Hub</p></div>
          <strong>🪙 68.02 BKC</strong>
        </header>

        <div className="level"><span /></div>

        <section className="hero">WELCOME<br/><small>GO BIKA MARKETPLACE</small></section>

        <div className="menu-grid">
          {menus.map(x => <button className="card" key={x}>{x}</button>)}
        </div>

        <h2 className="title">Supreme Character Catcher</h2><CharacterCatcher />
        <h2 className="title">Bika Characters</h2>
        <div className="nft-grid">
          {nfts.map(n => <article className="nft" key={n}><div className="image">NFT</div><b>{n}</b><p>Rare Character • Mystical</p><button>BUY NOW</button></article>)}
        </div>

        <div className="panels">
          <article>Wallet<br/><b>68.02 BKC</b><p>Transaction History</p></article>
          <article>Trade<br/><p>Send Character Request</p></article>
          <article>Auction<br/><p>Market Listings</p></article>
        </div>
      </section>
    </main>
  );
}
