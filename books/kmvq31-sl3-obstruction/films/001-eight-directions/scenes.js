'use strict';
// A symbolic film: every scene is a pure function of its own narration time.
function filmFade(S) { return clamp(S.u / 0.65) * clamp((S.d - S.u) / 0.5); }
function heading(en, zh, a) {
  txt(en, 110, 225, {size: 46, fam: F.disp, w: 700, c: C.cyan, a});
  txt(zh, 110, 285, {size: 34, fam: F.zh, c: C.white, a});
}
function equation(s, x, y, size, a, col = C.white) {
  txt(s, x, y, {size, fam: F.math, align: 'center', c: col, a});
}
function skewGrid(x, y, cell, n, a, reveal = 1) {
  for (let i = 0; i < n; i++) for (let j = 0; j < n; j++) {
    const col = i === j ? C.dim : i < j ? C.cyan : C.mag;
    box(x + j * cell, y + i * cell, cell - 5, cell - 5, col, a * reveal, 1.5);
    const label = i === j ? '0' : (i < j ? '' : '−') + 'x' + (Math.min(i,j)+1) + (Math.max(i,j)+1);
    equation(label, x + (j+0.5)*cell - 2, y + (i+0.6)*cell, cell*0.29, a*reveal, col);
  }
}
SCENES.table = S => {
  const a = filmFade(S); badge(a, 'argued');
  heading('A MULTIPLICATION TABLE', '从一张乘法表出发', a);
  const labels = [['×','u','e'],['u','u','0'],['e','0','u']];
  labels.forEach((row,i) => row.forEach((v,j) => {
    const col = i===0 || j===0 ? C.cyan : i===j ? C.mag : C.dim;
    chip(350+j*155, 420+i*120, 135, 95, v, col, a, 46, F.math);
  }));
  equation('u² = e² = u', 1290, 445, 65, a);
  equation('ue = 0', 1290, 555, 65, a * at(S,0,0.7), C.cyan);
  txt('e ↦ −e preserves every product', 1290, 695, {size:30,fam:F.disp,align:'center',c:C.white,a:a*at(S,2,0.7)});
};
SCENES.tiny = S => {
  const a=filmFade(S); badge(a,'argued');
  heading('COMPARE FIRST-ORDER TERMS', '比较一次项，就是乘积法则', a);
  equation('I + εD         ε² = 0',960,400,60,a);
  arrow(960,445,960,510,C.cyan,a*at(S,1,0.7));
  panel(230,540,1460,150,a*at(S,1,0.7),C.argued);
  equation('D(xy) = D(x)y + xD(y)',960,640,62,a*at(S,1,0.7));
  equation('[D, E] = DE − ED',960,800,47,a*at(S,2,0.7),C.cyan);
};
SCENES.blocks = S => {
  const a=filmFade(S);badge(a,'argued');
  heading('MIXED PRODUCTS FORCE CANCELLATION', '混合乘积为零，迫使系数相消',a);
  equation('dⱼᵢ eⱼ² + dᵢⱼ eᵢ² = 0',960,390,56,a);
  panel(110,450,760,340,a*at(S,1,0.8),C.cyan,'DIFFERENT SQUARE LINES');
  equation('eᵢ² ∦ eⱼ²',490,560,49,a*at(S,1,0.8));
  equation('dᵢⱼ = dⱼᵢ = 0',490,680,49,a*at(S,1,0.8),C.cyan);
  panel(960,450,840,340,a*at(S,1,0.8),C.mag,'EQUAL NORMALIZED SQUARES');
  equation('dⱼᵢ = −dᵢⱼ',1220,575,48,a*at(S,1,0.8),C.mag);
  skewGrid(1460,515,65,3,a,at(S,2,0.8));
  equation('Xᵀ = −X',1230,705,48,a*at(S,2,0.8));
};
SCENES.classify = S => {
  const a=filmFade(S);badge(a,'lean');
  heading('THE SEMISIMPLE CLASSIFICATION', '半单导子代数只能由正交块组成',a);
  txt('Algebraically closed field · characteristic zero',960,365,{size:31,fam:F.disp,align:'center',c:C.white,a});
  txt('A finite-dimensional evolution algebra · Der(A) semisimple',960,420,{size:28,fam:F.disp,align:'center',c:C.white,a});
  equation('Der(A) ≅ so(m₁) ⊕ ··· ⊕ so(mₛ)',960,495,62,a*at(S,1,0.8));
  for(let i=0;i<3;i++){
    const x=330+i*520;panel(x,550,390,170,a*at(S,1,0.8),C.cyan);
    equation(i===2?'···':'so(m'+(i===0?'₁':'₂')+')',x+195,650,52,a*at(S,1,0.8));
  }
  equation('mₐ ≥ 3       s = 0 is allowed',960,815,42,a*at(S,2,0.8));
};
SCENES.eight = S => {
  const a=filmFade(S);badge(a,'computed');
  heading('COUNT THE INDEPENDENT ENTRIES', '数一数独立坐标',a);
  equation('dim so(m) = m(m − 1)/2',960,390,58,a);
  [3,4,5].forEach((m,i)=>{
    const x=150+i*570;const dim=m*(m-1)/2;
    panel(x,455,500,210,a*at(S,1,0.65),i===2?C.dim:C.cyan);
    equation('m = '+m,x+250,535,42,a*at(S,1,0.65));
    equation(String(dim)+' dimensions',x+250,620,45,a*at(S,1,0.65),i===2?C.dim:C.cyan);
  });
  equation('dim sl(3) = 9 − 1 = 8',960,755,54,a*at(S,2,0.65),C.mag);
  equation('3a + 6b ≠ 8     (a, b ∈ ℕ₀)',960,840,48,a*at(S,2,0.65),C.white);
};
SCENES.bridge = S => {
  const a=filmFade(S);badge(a,'argued');
  heading('THE FULL GROUP MUST KEEP ITS TANGENT ALGEBRA', '全部群的同构必须保持切李代数',a);
  equation('det(I + εX) = 1 + ε tr(X)',960,405,56,a);
  panel(170,485,650,210,a*at(S,1,0.7),C.mag,'PROPOSED FULL GROUP');
  equation('Aut(A) ≅ SL(3)',495,615,52,a*at(S,1,0.7));
  arrow(850,590,1040,590,C.cyan,a*at(S,1,0.7));
  panel(1080,485,650,210,a*at(S,1,0.7),C.argued,'FORCED TANGENT ALGEBRA');
  equation('Der(A) ≅ sl(3)',1405,615,52,a*at(S,1,0.7));
  txt('Impossible: the orthogonal dimensions do not add up.',960,800,{size:37,fam:F.disp,align:'center',c:C.mag,a:a*at(S,1,0.7)});
};
SCENES.limits = S => {
  const a=filmFade(S);badge(a,'argued');
  heading('FULL GROUP ≠ SUBALGEBRA ACTION', '全部对称群，与子代数作用不同',a);
  panel(150,365,1620,160,a,C.argued);
  equation('No full SL(3) · no annihilator assumption',960,465,45,a);
  panel(150,570,760,200,a*at(S,1,0.7),C.cyan);
  txt('A faithful sl(3) action can exist.',530,650,{size:32,fam:F.disp,align:'center',c:C.white,a:a*at(S,1,0.7)});
  equation('sl(3) ↪ so(6)',530,725,44,a*at(S,1,0.7));
  panel(1010,570,760,200,a*at(S,1,0.7),C.open);
  txt('Abstract groups: outside this result',1390,680,{size:30,fam:F.disp,align:'center',c:C.white,a:a*at(S,1,0.7)});
  txt('Haobo Ma · Wenlin Zhang | version 2',960,845,{size:27,fam:F.disp,align:'center',c:C.dim,a});
};
FILM.poster = () => {
  txt('WHY EIGHT DIRECTIONS',110,270,{size:62,fam:F.disp,w:700,c:C.white});
  txt('CANNOT FIT',110,355,{size:74,fam:F.disp,w:700,c:C.cyan});
  txt('为什么八个方向装不进去？',110,440,{size:47,fam:F.zh,w:700,c:C.white});
  equation('dim sl(3) = 8',580,585,62,1,C.mag);
  equation('3a + 6b ≠ 8',580,705,70,1);
  txt('a, b count orthogonal blocks',580,775,{size:30,fam:F.disp,align:'center',c:C.dim});
  skewGrid(1160,300,145,3,1);
  txt('Sparse products → skew blocks → obstruction',110,850,{size:36,fam:F.disp,c:C.cyan});
  txt('Haobo Ma · Wenlin Zhang',110,925,{size:29,fam:F.disp,c:C.dim});
};
