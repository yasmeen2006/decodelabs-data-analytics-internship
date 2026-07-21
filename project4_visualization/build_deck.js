const pptxgen = require("pptxgenjs");

const INK = "2B2B2B";
const MUTED = "8A8A8A";
const ACCENT = "C0392B";
const BG = "FFFFFF";
const LIGHT_BG = "F7F7F7";

let pres = new pptxgen();
pres.layout = "LAYOUT_WIDE"; // 13.3 x 7.5

// ============================================================
// SLIDE 1 — TITLE
// ============================================================
let s1 = pres.addSlide();
s1.background = { color: BG };
s1.addText("Where Are We Losing Orders?", {
  x: 0.8, y: 2.5, w: 11.7, h: 1.2,
  fontSize: 40, bold: true, color: INK, fontFace: "Georgia", margin: 0,
});
s1.addText("An Order Fulfillment Analysis of 1,200 Transactions", {
  x: 0.8, y: 3.6, w: 11.7, h: 0.6,
  fontSize: 18, color: MUTED, fontFace: "Arial", margin: 0,
});
s1.addText("DecodeLabs Data Analytics Internship — Project 4  |  Prepared by Yasu", {
  x: 0.8, y: 6.7, w: 11.7, h: 0.4,
  fontSize: 12, color: MUTED, fontFace: "Arial", margin: 0,
});

// ============================================================
// SLIDE 2 — SITUATION
// ============================================================
let s2 = pres.addSlide();
s2.background = { color: BG };
s2.addText("Order Volume Has Been Steady — On the Surface, Business Looks Healthy", {
  x: 0.6, y: 0.5, w: 12.1, h: 1.0,
  fontSize: 26, bold: true, color: INK, fontFace: "Georgia", margin: 0,
});

const situationStats = [
  { label: "Total Orders Analyzed", value: "1,200" },
  { label: "Products in Catalog", value: "5" },
  { label: "Payment Methods Offered", value: "5" },
  { label: "Data Quality After Cleaning", value: "100%" },
];

const cardW = 2.75, gap = 0.35, startX = 0.6, cardY = 2.2, cardH = 2.0;
situationStats.forEach((stat, i) => {
  const x = startX + i * (cardW + gap);
  s2.addShape("roundRect", {
    x, y: cardY, w: cardW, h: cardH, rectRadius: 0.08,
    fill: { color: LIGHT_BG }, line: { type: "none" },
  });
  s2.addText(stat.value, {
    x, y: cardY + 0.35, w: cardW, h: 0.9,
    align: "center", fontSize: 34, bold: true, color: ACCENT, fontFace: "Georgia", margin: 0,
  });
  s2.addText(stat.label, {
    x: x + 0.15, y: cardY + 1.35, w: cardW - 0.3, h: 0.55,
    align: "center", fontSize: 12, color: MUTED, fontFace: "Arial", margin: 0,
  });
});

s2.addText(
  "The dataset passed every structural check: no duplicate IDs, no formatting errors, no calculation mismatches. Revenue is evenly distributed across the catalog — no single product carries disproportionate risk.",
  { x: 0.6, y: 4.7, w: 12.1, h: 1.2, fontSize: 15, color: INK, fontFace: "Arial", margin: 0, lineSpacingMultiple: 1.3 }
);

s2.addText("Situation", {
  x: 0.6, y: 6.9, w: 4, h: 0.4, fontSize: 11, color: MUTED, fontFace: "Arial", italic: true, margin: 0,
});

// ============================================================
// SLIDE 3 — COMPLICATION (the chart)
// ============================================================
let s3 = pres.addSlide();
s3.background = { color: BG };
s3.addText("But 41.4% of Orders Never Complete", {
  x: 0.6, y: 0.4, w: 12.1, h: 0.8,
  fontSize: 28, bold: true, color: INK, fontFace: "Georgia", margin: 0,
});
s3.addText("Cancelled and Returned orders combined outnumber Delivered orders outright.", {
  x: 0.6, y: 1.15, w: 12.1, h: 0.5,
  fontSize: 15, color: MUTED, fontFace: "Arial", margin: 0,
});

s3.addImage({
  path: "outputs/02_order_status_bar.png",
  x: 1.3, y: 1.85, w: 10.7, h: 5.1 * (10.7 / 13.5), // preserve aspect ratio approx
});

s3.addText("Complication", {
  x: 0.6, y: 6.9, w: 4, h: 0.4, fontSize: 11, color: MUTED, fontFace: "Arial", italic: true, margin: 0,
});

// ============================================================
// SLIDE 4 — RESOLUTION
// ============================================================
let s4 = pres.addSlide();
s4.background = { color: BG };
s4.addText("Recommendation: Investigate the Cancel/Return Funnel Before Scaling Spend", {
  x: 0.6, y: 0.5, w: 12.1, h: 1.1,
  fontSize: 25, bold: true, color: INK, fontFace: "Georgia", margin: 0,
});

const actions = [
  {
    h: "1. Root-cause the 41.4%",
    b: "Pull a sample of Cancelled and Returned orders and map them by stage — checkout, payment, fulfillment, or post-delivery — before assuming a single cause.",
  },
  {
    h: "2. Protect the high-value losses",
    b: "Cancelled orders priced above the dataset average represent the most expensive failures. Query 6 in Project 3 isolates these — that's the starting list.",
  },
  {
    h: "3. Report typical order value using the median",
    b: "Order value is right-skewed (mean ₹1,054 vs. median ₹824). Leading with the median avoids overstating what a normal customer actually spends.",
  },
];

let ry = 2.1;
actions.forEach((a) => {
  s4.addText(a.h, { x: 0.6, y: ry, w: 12.1, h: 0.45, fontSize: 16, bold: true, color: ACCENT, fontFace: "Arial", margin: 0 });
  s4.addText(a.b, { x: 0.6, y: ry + 0.42, w: 12.1, h: 0.7, fontSize: 13.5, color: INK, fontFace: "Arial", margin: 0, lineSpacingMultiple: 1.25 });
  ry += 1.35;
});

s4.addText("Resolution  |  Source: DecodeLabs Project 1–3 cleaned dataset, n=1,200 orders", {
  x: 0.6, y: 6.9, w: 12.1, h: 0.4, fontSize: 11, color: MUTED, fontFace: "Arial", italic: true, margin: 0,
});

pres.writeFile({ fileName: "Project4_Boardroom_Slide.pptx" }).then(() => {
  console.log("Deck written.");
});
