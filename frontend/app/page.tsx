export default function Home() {
  const menus = [
    'Rewards',
    'Wallet',
    'Gate',
    'Trade',
    'Cleaning',
    'Purchase',
    'NFT',
    'Auction'
  ];

  return (
    <main className="home">
      <h1>Bika Marketplace</h1>
      <p>BKC Character Trading Hub</p>

      <section className="menu-grid">
        {menus.map((item) => (
          <div className="card" key={item}>{item}</div>
        ))}
      </section>
    </main>
  );
}
