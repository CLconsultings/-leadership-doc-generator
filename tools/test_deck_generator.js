const {JSDOM}=require('jsdom'); const fs=require('fs');
const html=fs.readFileSync(require('path').join(__dirname,'deck-generator.html'),'utf8');
let printCalled=false,lastBlob=null;
const dom=new JSDOM(html,{runScripts:"dangerously",pretendToBeVisual:true,beforeParse(w){
  w.print=()=>{printCalled=true;};
  w.URL.createObjectURL=(b)=>{lastBlob=b;return "blob:mock";};
  w.URL.revokeObjectURL=()=>{};
}});
const {window}=dom, {document}=window;
let fail=0; const chk=(c,m)=>{if(!c){console.log("FAIL:",m);fail++;}else{console.log("ok  :",m);}};
const H=()=>document.getElementById("deck").innerHTML;
const click=sel=>{const el=typeof sel==="string"?document.querySelector(sel):sel;
  el.dispatchEvent(new window.Event("click",{bubbles:true}));};

(async()=>{
  // initial render
  chk(document.querySelectorAll("#deck .slide").length===9,"initial: 9 slides render");
  chk(H().includes("Managers in Motion"),"initial: default program = Managers");

  // program select
  const sel=document.getElementById("program"); sel.value="teams";
  sel.dispatchEvent(new window.Event("change",{bubbles:true}));
  chk(H().includes("Clarify the work"),"program select -> Teams content");

  // design Option 2 (all B)
  click('#design button[data-d="b"]');
  chk(H().includes('class="divb"')&&H().includes('quote'),"Design Option 2 -> all slides design B");
  chk(document.querySelector('#design button[data-d="b"]').getAttribute("aria-pressed")==="true","Option 2 pressed");

  // design Option 1 (all A)
  click('#design button[data-d="a"]');
  chk(H().includes('class="divwrap"')&&H().includes('class="lead"'),"Design Option 1 -> all slides design A");

  // per-slide A|B: flip the first slide (title) to B
  click('#deck .slide:first-child .dtb[data-s="b"]');
  chk(document.querySelector('#deck .slide:first-child').innerHTML.includes("fill center"),"per-slide B toggle flips just that slide");
  chk(document.querySelector('#deck .slide:first-child .dtb[data-s="b"]').getAttribute("aria-pressed")==="true","that slide's B pressed");

  // reset
  click('#reset');
  chk(H().includes('class="divwrap"'),"Reset -> back to design A");
  chk(document.querySelector('#design button[data-d="a"]').getAttribute("aria-pressed")==="true","Reset -> Option 1 pressed");

  // download settings
  click('#spec');
  chk(lastBlob!==null,"Download settings -> Blob created");
  const txt=await lastBlob.text(); let spec=null; try{spec=JSON.parse(txt);}catch(e){}
  chk(spec&&spec.name&&Array.isArray(spec.items)&&spec.spot&&spec.bigIdea,"Download settings -> valid JSON spec");

  // print
  click('#print');
  chk(printCalled,"Print -> window.print() called");

  console.log(fail===0?"\nALL BUTTONS FUNCTIONAL":"\n"+fail+" BUTTON FAILURES");
  process.exit(fail?1:0);
})();
