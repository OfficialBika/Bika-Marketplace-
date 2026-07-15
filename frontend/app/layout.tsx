import './globals.css';

export const metadata = {
 title: 'Bika Marketplace | Supreme Character Hub',
 description: 'BKC Character Trading, NFT Marketplace, Auction and Premium Collectibles Hub'
};

export default function RootLayout({children}:{children: React.ReactNode}) {
 return (
  <html lang="en">
   <body>{children}</body>
  </html>
 );
}
