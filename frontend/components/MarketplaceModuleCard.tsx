"use client";

export default function MarketplaceModuleCard({title,description,action}:{title:string;description:string;action?:()=>void}){
 return (
  <button onClick={action} className="market-module-card">
   <h3>{title}</h3>
   <p>{description}</p>
  </button>
 );
}
