function gcd(r0,r1) {
 var x0 = 1;
 var x1 = 0;
 var p = r1;
 while(r1 != 0)
 {
  var q1 = Math.floor(r0/r1);
  var r2 = r0 - r1*q1;
  r0 = r1; r1 = r2;
  var x = x0;
  x0 = x1;
  x1 = x - q1*x1;
 }
 if(x0 < 0)
 {
  x0 -= Math.floor(x0/p)*p;
 }
 return {gcd: r0, inv: x0};
}

function sgrp(g,n) {
 var i=g;
 var grp = [i];
 while(i != 1)
 {
  i = (i*g) % n;
  grp.push(i);
 }
 return grp;
}

function modexp(g,n,m) {
 var r=g;
 for(var i=1; i<n; i++) {
  r=r*g%m;
 }
 return r;
}

function divs(n) {
 var d=[];
 for(var i=0; i<=n; i++) {
  if(n%i==0) {
   d.push(i);
  }
 }
 return d;
}

function rc(n) {
 var residue = [];
 for(var i=1; i<n; i++) {
  if(gcd(i,n).gcd==1) {
   residue.push(i);
  }
 }
 return residue;
}

function order(g,n) {
 var residues = rc(n);
 var phi = residues.length;
 var d = divs(phi);
 
 for(var i=0; i<d.length; i++) {
  if(modexp(g,d[i],n)==1) {
   return d[i];
  }
 }
 return -1;
}

function setleq(a,b) {
  vals = a.values();
  for(var v=0; v<vals.length; v++) {
   if(!b.has(vals[v])) {
    return false;
   }
  }
  return true;
 }
 
 function seteq(a,b) {
  if(a.size()!=b.size()) {return false;}
  return setleq(a,b) && setleq(b,a);
 }

function createSvg(elements, root, n, subgroups, div) {
 var width = 300;
 var w2 = width/2;
 
 var svg = d3.select(div)
  .append("svg")
  .attr("width", width)
  .attr("height", width);
 
 var r=root;
 var root_order=1;
 var perm = [r];
 while(r!=1) {
  r=r*root%n;
  perm.push(r);
  root_order++;
 }
 var lkp = d3.scale.ordinal().domain(perm).range(d3.range(0,root_order));
 
 svg.append("circle")
  .attr("cx",w2)
  .attr("cy",w2)
  .attr("r",w2-30)
  .attr("fill","none")
  .attr("stroke","#aaa");
   
 var elm = svg.selectAll(".element")
  .attr("class","element")
  .data(d3.range(0,359,(360/root_order)))
  .enter()
  .append("g")
  .attr("transform", function(d) {
          return "translate(" + w2 + "," + 30 + ") rotate(" + d + ",0," + (w2-30) + ")";});
  
 elm.append("text")
  .attr("text-anchor","middle")
  .text(function(d,i) { return perm[i]; })
  .attr("font-weight",function(d,i) { return i==0 ? "bold" : "normal"; })
  .attr("fill", "#444")
  .attr("font-size", function(d,i) {return i==0 ? "16px" : "12px";})
  .attr("dy",function(d,i) {return i==0 ? "-16px" : "-4px";});
  
 elm.append("circle")
  .attr("r","2px")
  .attr("fill","black");
  
 num_coord = function(c) {
  pos = lkp(c)*2*Math.PI/root_order-Math.PI/2;
  return {x: (w2+(w2-30)*Math.cos(pos)),
          y: (w2+(w2-30)*Math.sin(pos))};
 }
  
 var sgrp_line = d3.svg.line()
  .x(function(d) {return d.x;})
  .y(function(d) {return d.y;})
  .interpolate("linear");
 
 var csc = d3.scale.category20();
 var ps = d3.set(perm);
 var subgroups_cont = subgroups.filter(function(d) {return setleq(d.grp,ps);});
 svg.selectAll(".subgroup")
  .attr("class","subgroup")
  .data(subgroups_cont)
  .enter()
  .append("path")
  .attr("d",function(d) {
   var s = d.ordered;
   var line_data = [];
   for(var i=0; i<s.length; i++) {
    line_data.push(num_coord(s[i]));
   }
   line_data.push(num_coord(s[0]));
   return sgrp_line(line_data);
  })
  .attr("stroke",function(d,i) {return csc(i);})
  .attr("fill","none");
  
 svg.append("text")
  .attr("fill","#444")
  .attr("font-size","16px")
  .attr("text-anchor","middle")
  .attr("dominant-baseline","central")
  .text("" + perm.length)
  .attr("transform","translate(" + w2 + "," + w2 + ")");
}

function drawGroup(n,div) {
 if(n<2 || n>3000) {return;}
 var elements = [];
 for(var i=1; i<n; i++) {
  var g = gcd(i,n);
  if(g.gcd == 1) {
   elements.push({num: i, inv: g.inv, ord: order(i,n)});
  }
 }
 
 var subgroups = [];
 for(var i=0; i<elements.length; i++) {
  var sg_o = sgrp(elements[i].num,n);
  var sg = d3.set(sg_o);
  var ok=true;
  for(var s=0; s<subgroups.length; s++) {
   if(seteq(sg,subgroups[s].grp)) {
    subgroups[s].gen.add(elements[i].num);
    ok=false;
    break;
   }
  }
  if(ok) {
   subgroups.push({gen: d3.set([elements[i].num]), grp: sg, ordered: sg_o});
  }
 }
 for(var i=0; i<subgroups.length; i++) {
  createSvg(elements,Object.keys(subgroups[i].gen._)[0],n,subgroups,div);
 }
}

window.onload = function() {
 drawGroup(13,"#grp-holder");
 document.getElementById("go").onclick = function() {
  document.getElementById("grp2-holder").innerHTML = "";
  drawGroup(document.getElementById("n").value,"#grp2-holder");
 }
}
