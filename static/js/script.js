const $ = (s, p=document) => p.querySelector(s);
const $$ = (s, p=document) => [...p.querySelectorAll(s)];

function toast(message, type="info"){
  const el = document.createElement("div");
  el.className = "toast align-items-center text-bg-dark border-0 show mb-2";
  el.innerHTML = `<div class="d-flex"><div class="toast-body">${escapeHtml(message)}</div><button class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast"></button></div>`;
  $("#toastContainer")?.appendChild(el);
  setTimeout(()=>el.remove(), 3500);
}
function escapeHtml(value){
  return String(value ?? "").replace(/[&<>"']/g, m => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#039;'}[m]));
}
async function api(url, options={}){
  const res = await fetch(url, {headers:{"Content-Type":"application/json", ...(options.headers||{})}, ...options});
  const data = await res.json().catch(()=>({success:false,error:"Unexpected server response."}));
  if(!res.ok) throw new Error(data.error || "Request failed.");
  return data;
}
function setupPasswordToggles(){
  $$(".toggle-password").forEach(btn=>{
    btn.addEventListener("click", ()=>{
      const input = document.getElementById(btn.dataset.target);
      if(!input) return;
      input.type = input.type === "password" ? "text" : "password";
      btn.innerHTML = input.type === "password" ? "👁" : "🙈";
    });
  });
}
function setupSidebar(){
  const side = $("#sidebar"), toggle = $("#sidebarToggle");
  toggle?.addEventListener("click", ()=>side?.classList.toggle("show"));
}
function setupLogout(){
  $$(".logout-btn").forEach(btn=>btn.addEventListener("click", async ()=>{
    try{ await api("/api/logout",{method:"POST"}); location.href="/"; }catch(e){ toast(e.message,"danger"); }
  }));
}
document.addEventListener("DOMContentLoaded", ()=>{setupPasswordToggles();setupSidebar();setupLogout();});
