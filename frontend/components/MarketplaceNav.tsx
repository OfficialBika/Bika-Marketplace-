"use client";

import Link from 'next/link';

export default function MarketplaceNav(){
 return (
  <nav className="marketplace-nav flex gap-4">
   <Link href="/marketplace">Marketplace</Link>
   <Link href="/auction">Auction</Link>
   <Link href="/wallet">Wallet</Link>
   <Link href="/trade">Trade</Link>
  </nav>
 );
}
