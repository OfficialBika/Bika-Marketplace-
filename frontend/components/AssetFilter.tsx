"use client";

export default function AssetFilter(){
 return (
  <div className="asset-filter rounded-xl border p-4">
   <label>Filter Assets</label>
   <select className="ml-3 rounded-lg border p-2">
    <option>All</option>
    <option>Rare</option>
    <option>Supreme</option>
   </select>
  </div>
 );
}
