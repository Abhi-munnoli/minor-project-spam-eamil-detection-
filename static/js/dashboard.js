document.addEventListener("DOMContentLoaded", async ()=>{
  if(!$("#analyzerForm")) return;
  const textarea=$("#message"), counter=$("#charCount"), result=$("#result"), analyze=$("#analyzeBtn");
  textarea?.addEventListener("input",()=>{counter.textContent=textarea.value.length.toLocaleString();});
  $("#clearBtn")?.addEventListener("click",()=>{textarea.value="";counter.textContent="0";result.style.display="none";});
  $("#analyzerForm").addEventListener("submit",async e=>{
    e.preventDefault();
    const message=textarea.value.trim();
    if(!message){toast("Paste an email or message first.","warning");return;}
    analyze.disabled=true; analyze.innerHTML=`<span class="spinner-border spinner-border-sm me-2"></span>Analyzing...`;
    try{
      const d=await api("/api/predict",{method:"POST",body:JSON.stringify({message})});
      result.className=`result ${d.prediction==="Spam"?"spam":"ham"}`;
      result.style.display="block";
      const spam=d.prediction==="Spam";
      $("#resultIcon").textContent=spam?"⚠️":"✓";
      $("#resultTitle").textContent=spam?"SPAM DETECTED":"NOT SPAM";
      $("#resultText").textContent=spam?"This message appears to be spam.":"This message appears to be safe.";
      $("#confidence").textContent=`${d.confidence.toFixed(2)}%`;
      $("#confidenceBar").style.width=`${d.confidence}%`;
      $("#classification").textContent=d.prediction;
      $("#messageLength").textContent=d.message_length.toLocaleString();
      $("#analysisTime").textContent=`${d.analysis_ms} ms`;
      $("#analysisDate").textContent=new Date(d.analyzed_at).toLocaleString();
      $("#explanation").textContent=spam
        ?"The model detected patterns commonly associated with spam messages."
        :"The model did not detect strong spam patterns in this message.";
      result.scrollIntoView({behavior:"smooth",block:"nearest"});
      loadStats();
    }catch(err){toast(err.message,"danger");}
    finally{analyze.disabled=false;analyze.innerHTML=`Analyze Message <span class="ms-2">→</span>`;}
  });
  loadStats();
});
async function loadStats(){
  try{
    const d=await api("/api/stats");
    $("#totalScans") && ($("#totalScans").textContent=d.stats.total);
    $("#spamCount") && ($("#spamCount").textContent=d.stats.spam);
    $("#safeCount") && ($("#safeCount").textContent=d.stats.safe);
    $("#detectionRate") && ($("#detectionRate").textContent=`${d.stats.rate}%`);
  }catch(_){}
}
