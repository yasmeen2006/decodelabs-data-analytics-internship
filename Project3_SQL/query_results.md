# Project 3 — SQL Query Results

Run against `decodelabs.db` (SQLite, built from the Project 1 cleaned dataset).

## 1. Basic SELECT + WHERE

```sql
SELECT OrderID, CustomerID, Product, TotalPrice, OrderStatus
FROM orders
WHERE TotalPrice > 2000
ORDER BY TotalPrice DESC;
```

| OrderID   | CustomerID   | Product   |   TotalPrice | OrderStatus   |
|:----------|:-------------|:----------|-------------:|:--------------|
| ORD200789 | C57276       | Tablet    |      3456.4  | Delivered     |
| ORD201122 | C38840       | Monitor   |      3390.95 | Returned      |
| ORD200632 | C67260       | Laptop    |      3390.8  | Delivered     |
| ORD200469 | C13877       | Chair     |      3384.9  | Cancelled     |
| ORD200328 | C18404       | Tablet    |      3370.2  | Cancelled     |
| ORD200107 | C16775       | Printer   |      3353.75 | Shipped       |
| ORD200326 | C65986       | Laptop    |      3352.4  | Returned      |
| ORD201065 | C47778       | Printer   |      3334    | Delivered     |
| ORD201031 | C59183       | Phone     |      3322.55 | Pending       |
| ORD200463 | C25276       | Laptop    |      3313.9  | Shipped       |
| ORD200361 | C53464       | Printer   |      3299.25 | Delivered     |
| ORD200367 | C13108       | Laptop    |      3293.85 | Pending       |
| ORD200837 | C88029       | Chair     |      3277.75 | Delivered     |
| ORD200527 | C27202       | Chair     |      3267.35 | Cancelled     |
| ORD200768 | C35987       | Tablet    |      3267.3  | Cancelled     |
| ORD200889 | C36725       | Monitor   |      3253.6  | Cancelled     |
| ORD200540 | C87281       | Laptop    |      3243.25 | Pending       |
| ORD200802 | C84331       | Chair     |      3223.2  | Cancelled     |
| ORD200957 | C73575       | Monitor   |      3219.45 | Returned      |
| ORD200086 | C88205       | Printer   |      3215.15 | Cancelled     |
| ORD200221 | C93473       | Tablet    |      3196.85 | Pending       |
| ORD200967 | C52879       | Tablet    |      3194.6  | Returned      |
| ORD200296 | C48453       | Desk      |      3194    | Cancelled     |
| ORD201079 | C89979       | Phone     |      3170    | Delivered     |
| ORD200364 | C85282       | Phone     |      3143.7  | Cancelled     |
| ORD200764 | C35983       | Laptop    |      3137.15 | Cancelled     |
| ORD200010 | C43443       | Tablet    |      3129.85 | Returned      |
| ORD200820 | C35377       | Phone     |      3119.05 | Returned      |
| ORD200097 | C15624       | Tablet    |      3097.6  | Pending       |
| ORD200241 | C20817       | Chair     |      3078.35 | Pending       |
| ORD200450 | C36408       | Monitor   |      3075.5  | Returned      |
| ORD200876 | C90363       | Chair     |      3044.55 | Pending       |
| ORD200492 | C39074       | Laptop    |      3032.6  | Shipped       |
| ORD200633 | C79533       | Laptop    |      3008.6  | Cancelled     |
| ORD200731 | C71310       | Printer   |      2922.3  | Returned      |
| ORD200916 | C35669       | Printer   |      2894.15 | Returned      |
| ORD200511 | C11415       | Monitor   |      2876.2  | Delivered     |
| ORD200816 | C55286       | Tablet    |      2873.95 | Pending       |
| ORD200000 | C72649       | Monitor   |      2853.1  | Shipped       |
| ORD200578 | C50415       | Monitor   |      2830.35 | Delivered     |
| ORD200883 | C43595       | Printer   |      2807.4  | Delivered     |
| ORD201002 | C83911       | Tablet    |      2799.52 | Pending       |
| ORD200628 | C18717       | Printer   |      2793.15 | Pending       |
| ORD200389 | C29703       | Desk      |      2790    | Shipped       |
| ORD201153 | C98317       | Monitor   |      2786.84 | Shipped       |
| ORD201142 | C23405       | Phone     |      2780.4  | Returned      |
| ORD200222 | C43124       | Chair     |      2773.44 | Shipped       |
| ORD201087 | C84134       | Laptop    |      2772.28 | Shipped       |
| ORD200223 | C22783       | Phone     |      2771.64 | Pending       |
| ORD201156 | C20512       | Laptop    |      2763.12 | Shipped       |
| ORD200471 | C52717       | Desk      |      2756.35 | Cancelled     |
| ORD200002 | C81728       | Tablet    |      2753.4  | Cancelled     |
| ORD201076 | C99116       | Laptop    |      2746.44 | Shipped       |
| ORD200423 | C94311       | Printer   |      2740.8  | Cancelled     |
| ORD200608 | C32956       | Laptop    |      2715.8  | Cancelled     |
| ORD200769 | C13366       | Printer   |      2714.2  | Delivered     |
| ORD200865 | C72241       | Monitor   |      2709.48 | Pending       |
| ORD200032 | C12388       | Tablet    |      2683.6  | Delivered     |
| ORD200164 | C70566       | Desk      |      2682.9  | Pending       |
| ORD200252 | C19648       | Phone     |      2673.44 | Cancelled     |
| ORD200694 | C92049       | Printer   |      2666.08 | Shipped       |
| ORD200269 | C48942       | Tablet    |      2654.68 | Pending       |
| ORD200170 | C80223       | Desk      |      2651.76 | Cancelled     |
| ORD200963 | C88075       | Chair     |      2651.7  | Shipped       |
| ORD200394 | C70148       | Desk      |      2647.75 | Shipped       |
| ORD200523 | C65083       | Desk      |      2631.16 | Returned      |
| ORD200781 | C43524       | Phone     |      2621.3  | Delivered     |
| ORD200287 | C70437       | Chair     |      2620.72 | Shipped       |
| ORD200281 | C87181       | Desk      |      2619.16 | Pending       |
| ORD200823 | C27070       | Laptop    |      2612.52 | Shipped       |
| ORD200683 | C91591       | Desk      |      2609.92 | Pending       |
| ORD200340 | C76207       | Laptop    |      2606.25 | Cancelled     |
| ORD200707 | C31761       | Chair     |      2600.16 | Cancelled     |
| ORD200977 | C85841       | Chair     |      2597.88 | Pending       |
| ORD201094 | C66093       | Printer   |      2595.64 | Shipped       |
| ORD201179 | C84630       | Laptop    |      2592.75 | Cancelled     |
| ORD200986 | C69213       | Laptop    |      2579.84 | Pending       |
| ORD200587 | C18820       | Monitor   |      2573    | Delivered     |
| ORD200465 | C58773       | Printer   |      2567.45 | Cancelled     |
| ORD200282 | C30411       | Printer   |      2551.16 | Cancelled     |
| ORD200446 | C89592       | Laptop    |      2547.9  | Delivered     |
| ORD200390 | C55996       | Printer   |      2543.45 | Delivered     |
| ORD200500 | C79475       | Laptop    |      2542.95 | Returned      |
| ORD201144 | C88463       | Desk      |      2539.7  | Cancelled     |
| ORD200607 | C96434       | Printer   |      2536.2  | Shipped       |
| ORD201097 | C81370       | Monitor   |      2532.25 | Shipped       |
| ORD200549 | C34266       | Monitor   |      2519.52 | Cancelled     |
| ORD200120 | C58108       | Tablet    |      2517.36 | Cancelled     |
| ORD200872 | C59169       | Chair     |      2517.36 | Shipped       |
| ORD200118 | C27898       | Printer   |      2513.55 | Shipped       |
| ORD200558 | C76766       | Phone     |      2512.48 | Delivered     |
| ORD200925 | C78500       | Monitor   |      2512.35 | Shipped       |
| ORD200345 | C24751       | Tablet    |      2506.3  | Shipped       |
| ORD200004 | C81840       | Printer   |      2504.04 | Delivered     |
| ORD200114 | C77272       | Monitor   |      2492.4  | Pending       |
| ORD200598 | C60329       | Desk      |      2476.75 | Pending       |
| ORD200567 | C92575       | Chair     |      2464.7  | Shipped       |
| ORD200091 | C98216       | Laptop    |      2463.75 | Shipped       |
| ORD200457 | C50236       | Desk      |      2463.32 | Returned      |
| ORD200994 | C27613       | Tablet    |      2462.6  | Delivered     |
| ORD200311 | C71698       | Desk      |      2446.85 | Returned      |
| ORD200486 | C88981       | Printer   |      2445.04 | Shipped       |
| ORD200798 | C20861       | Phone     |      2441.75 | Returned      |
| ORD200832 | C63372       | Chair     |      2428.55 | Pending       |
| ORD200359 | C95643       | Desk      |      2426.28 | Delivered     |
| ORD200174 | C51145       | Printer   |      2403.24 | Delivered     |
| ORD200817 | C87994       | Chair     |      2392.76 | Delivered     |
| ORD200801 | C97593       | Printer   |      2382.48 | Pending       |
| ORD200621 | C37455       | Phone     |      2380.05 | Delivered     |
| ORD200913 | C45599       | Printer   |      2379.75 | Returned      |
| ORD200059 | C97603       | Chair     |      2373.08 | Shipped       |
| ORD200688 | C20077       | Monitor   |      2372.88 | Cancelled     |
| ORD200805 | C59278       | Laptop    |      2360.05 | Cancelled     |
| ORD200360 | C53810       | Phone     |      2358.28 | Pending       |
| ORD200072 | C19451       | Tablet    |      2357.76 | Returned      |
| ORD200560 | C33634       | Monitor   |      2355.4  | Pending       |
| ORD200267 | C84480       | Chair     |      2342.55 | Delivered     |
| ORD200490 | C50097       | Chair     |      2339.05 | Cancelled     |
| ORD200266 | C38840       | Chair     |      2332.28 | Cancelled     |
| ORD200342 | C69994       | Monitor   |      2332.1  | Returned      |
| ORD200726 | C18105       | Laptop    |      2332.08 | Delivered     |
| ORD201080 | C70613       | Laptop    |      2323.7  | Delivered     |
| ORD200965 | C70412       | Laptop    |      2313.12 | Cancelled     |
| ORD200638 | C66840       | Tablet    |      2313.08 | Delivered     |
| ORD200588 | C61849       | Monitor   |      2311.28 | Delivered     |
| ORD200838 | C57798       | Desk      |      2308.32 | Pending       |
| ORD201124 | C33744       | Chair     |      2307.48 | Returned      |
| ORD200034 | C67195       | Chair     |      2306.08 | Pending       |
| ORD200615 | C97218       | Monitor   |      2300.7  | Returned      |
| ORD200541 | C69009       | Printer   |      2280.3  | Pending       |
| ORD200089 | C17181       | Printer   |      2276.65 | Cancelled     |
| ORD200641 | C71680       | Printer   |      2270.28 | Pending       |
| ORD200082 | C65799       | Tablet    |      2260.8  | Shipped       |
| ORD201199 | C57502       | Tablet    |      2242.32 | Returned      |
| ORD200575 | C74005       | Chair     |      2240.75 | Returned      |
| ORD201041 | C21167       | Monitor   |      2235.6  | Shipped       |
| ORD200151 | C32960       | Printer   |      2223.8  | Returned      |
| ORD201027 | C93467       | Laptop    |      2219.32 | Returned      |
| ORD200046 | C43212       | Monitor   |      2200.56 | Pending       |
| ORD200309 | C63153       | Chair     |      2199.04 | Delivered     |
| ORD200407 | C85993       | Tablet    |      2189.28 | Returned      |
| ORD200858 | C22167       | Tablet    |      2178.3  | Pending       |
| ORD200200 | C97681       | Tablet    |      2166.3  | Delivered     |
| ORD200083 | C15681       | Laptop    |      2161.64 | Cancelled     |
| ORD201047 | C81726       | Chair     |      2161.36 | Shipped       |
| ORD200283 | C39638       | Laptop    |      2161.32 | Shipped       |
| ORD200177 | C55632       | Chair     |      2158.45 | Pending       |
| ORD200670 | C14576       | Desk      |      2156.8  | Pending       |
| ORD200189 | C48939       | Printer   |      2147.25 | Cancelled     |
| ORD201155 | C41478       | Printer   |      2138.28 | Delivered     |
| ORD200153 | C71570       | Chair     |      2137.92 | Returned      |
| ORD200737 | C91029       | Phone     |      2131.48 | Pending       |
| ORD200713 | C65056       | Tablet    |      2129.96 | Cancelled     |
| ORD200399 | C64641       | Tablet    |      2119.65 | Returned      |
| ORD201146 | C36383       | Monitor   |      2107.2  | Pending       |
| ORD200573 | C13205       | Chair     |      2107.1  | Cancelled     |
| ORD201006 | C27435       | Tablet    |      2104.9  | Delivered     |
| ORD200491 | C98168       | Phone     |      2103.5  | Pending       |
| ORD200742 | C41974       | Laptop    |      2099.79 | Returned      |
| ORD200736 | C59441       | Monitor   |      2092.65 | Pending       |
| ORD200935 | C39593       | Phone     |      2078.13 | Delivered     |
| ORD200771 | C20357       | Phone     |      2077.32 | Cancelled     |
| ORD201171 | C39911       | Phone     |      2073.6  | Delivered     |
| ORD201034 | C84524       | Printer   |      2071.92 | Cancelled     |
| ORD200653 | C59338       | Printer   |      2070.9  | Shipped       |
| ORD200885 | C61090       | Laptop    |      2062.36 | Shipped       |
| ORD200429 | C38126       | Printer   |      2060.76 | Pending       |
| ORD200141 | C80004       | Printer   |      2052.42 | Cancelled     |
| ORD200288 | C97643       | Laptop    |      2051    | Returned      |
| ORD200178 | C53070       | Chair     |      2048.24 | Delivered     |
| ORD200304 | C86762       | Monitor   |      2043.65 | Delivered     |
| ORD200357 | C74982       | Laptop    |      2042.8  | Delivered     |
| ORD200458 | C31412       | Monitor   |      2042.32 | Returned      |
| ORD200009 | C31946       | Desk      |      2037.52 | Shipped       |
| ORD200807 | C82344       | Monitor   |      2028.63 | Delivered     |
| ORD201035 | C70315       | Laptop    |      2024.44 | Cancelled     |
| ORD200181 | C38966       | Printer   |      2021.95 | Shipped       |
| ORD200915 | C20643       | Laptop    |      2011.96 | Shipped       |
| ORD200979 | C75018       | Monitor   |      2007.18 | Delivered     |
| ORD201136 | C71899       | Tablet    |      2004.99 | Pending       |

## 2. ORDER BY — top 10 highest-value orders overall

```sql
SELECT OrderID, Product, Quantity, UnitPrice, TotalPrice
FROM orders
ORDER BY TotalPrice DESC
LIMIT 10;
```

| OrderID   | Product   |   Quantity |   UnitPrice |   TotalPrice |
|:----------|:----------|-----------:|------------:|-------------:|
| ORD200789 | Tablet    |          5 |      691.28 |      3456.4  |
| ORD201122 | Monitor   |          5 |      678.19 |      3390.95 |
| ORD200632 | Laptop    |          5 |      678.16 |      3390.8  |
| ORD200469 | Chair     |          5 |      676.98 |      3384.9  |
| ORD200328 | Tablet    |          5 |      674.04 |      3370.2  |
| ORD200107 | Printer   |          5 |      670.75 |      3353.75 |
| ORD200326 | Laptop    |          5 |      670.48 |      3352.4  |
| ORD201065 | Printer   |          5 |      666.8  |      3334    |
| ORD201031 | Phone     |          5 |      664.51 |      3322.55 |
| ORD200463 | Laptop    |          5 |      662.78 |      3313.9  |

## 3. GROUP BY + COUNT — order volume per product

```sql
SELECT Product, COUNT(*) AS OrderCount
FROM orders
GROUP BY Product
ORDER BY OrderCount DESC;
```

| Product   |   OrderCount |
|:----------|-------------:|
| Printer   |          181 |
| Tablet    |          179 |
| Chair     |          178 |
| Laptop    |          173 |
| Desk      |          170 |
| Monitor   |          163 |
| Phone     |          156 |

## 4. GROUP BY + SUM — total revenue per product

```sql
SELECT Product, SUM(TotalPrice) AS TotalRevenue
FROM orders
GROUP BY Product
ORDER BY TotalRevenue DESC;
```

| Product   |   TotalRevenue |
|:----------|---------------:|
| Chair     |         195620 |
| Printer   |         195613 |
| Laptop    |         192127 |
| Tablet    |         186569 |
| Monitor   |         175651 |
| Desk      |         167460 |
| Phone     |         151722 |

## 5. GROUP BY + AVG — average order value per payment method

```sql
SELECT PaymentMethod, ROUND(AVG(TotalPrice), 2) AS AvgOrderValue, COUNT(*) AS Orders
FROM orders
GROUP BY PaymentMethod
ORDER BY AvgOrderValue DESC;
```

| PaymentMethod   |   AvgOrderValue |   Orders |
|:----------------|----------------:|---------:|
| Credit Card     |         1127.55 |      234 |
| Gift Card       |         1070.97 |      230 |
| Cash            |         1056.04 |      246 |
| Online          |         1017.22 |      258 |
| Debit Card      |         1001.56 |      232 |

## 6. WHERE with multiple conditions — cancelled orders above the overall average value

```sql
SELECT OrderID, CustomerID, Product, TotalPrice, OrderStatus
FROM orders
WHERE OrderStatus = 'Cancelled'
  AND TotalPrice > (SELECT AVG(TotalPrice) FROM orders)
ORDER BY TotalPrice DESC;
```

| OrderID   | CustomerID   | Product   |   TotalPrice | OrderStatus   |
|:----------|:-------------|:----------|-------------:|:--------------|
| ORD200469 | C13877       | Chair     |      3384.9  | Cancelled     |
| ORD200328 | C18404       | Tablet    |      3370.2  | Cancelled     |
| ORD200527 | C27202       | Chair     |      3267.35 | Cancelled     |
| ORD200768 | C35987       | Tablet    |      3267.3  | Cancelled     |
| ORD200889 | C36725       | Monitor   |      3253.6  | Cancelled     |
| ORD200802 | C84331       | Chair     |      3223.2  | Cancelled     |
| ORD200086 | C88205       | Printer   |      3215.15 | Cancelled     |
| ORD200296 | C48453       | Desk      |      3194    | Cancelled     |
| ORD200364 | C85282       | Phone     |      3143.7  | Cancelled     |
| ORD200764 | C35983       | Laptop    |      3137.15 | Cancelled     |
| ORD200633 | C79533       | Laptop    |      3008.6  | Cancelled     |
| ORD200471 | C52717       | Desk      |      2756.35 | Cancelled     |
| ORD200002 | C81728       | Tablet    |      2753.4  | Cancelled     |
| ORD200423 | C94311       | Printer   |      2740.8  | Cancelled     |
| ORD200608 | C32956       | Laptop    |      2715.8  | Cancelled     |
| ORD200252 | C19648       | Phone     |      2673.44 | Cancelled     |
| ORD200170 | C80223       | Desk      |      2651.76 | Cancelled     |
| ORD200340 | C76207       | Laptop    |      2606.25 | Cancelled     |
| ORD200707 | C31761       | Chair     |      2600.16 | Cancelled     |
| ORD201179 | C84630       | Laptop    |      2592.75 | Cancelled     |
| ORD200465 | C58773       | Printer   |      2567.45 | Cancelled     |
| ORD200282 | C30411       | Printer   |      2551.16 | Cancelled     |
| ORD201144 | C88463       | Desk      |      2539.7  | Cancelled     |
| ORD200549 | C34266       | Monitor   |      2519.52 | Cancelled     |
| ORD200120 | C58108       | Tablet    |      2517.36 | Cancelled     |
| ORD200688 | C20077       | Monitor   |      2372.88 | Cancelled     |
| ORD200805 | C59278       | Laptop    |      2360.05 | Cancelled     |
| ORD200490 | C50097       | Chair     |      2339.05 | Cancelled     |
| ORD200266 | C38840       | Chair     |      2332.28 | Cancelled     |
| ORD200965 | C70412       | Laptop    |      2313.12 | Cancelled     |
| ORD200089 | C17181       | Printer   |      2276.65 | Cancelled     |
| ORD200083 | C15681       | Laptop    |      2161.64 | Cancelled     |
| ORD200189 | C48939       | Printer   |      2147.25 | Cancelled     |
| ORD200713 | C65056       | Tablet    |      2129.96 | Cancelled     |
| ORD200573 | C13205       | Chair     |      2107.1  | Cancelled     |
| ORD200771 | C20357       | Phone     |      2077.32 | Cancelled     |
| ORD201034 | C84524       | Printer   |      2071.92 | Cancelled     |
| ORD200141 | C80004       | Printer   |      2052.42 | Cancelled     |
| ORD201035 | C70315       | Laptop    |      2024.44 | Cancelled     |
| ORD200746 | C32183       | Desk      |      1985.67 | Cancelled     |
| ORD200911 | C80872       | Desk      |      1984.3  | Cancelled     |
| ORD200216 | C70492       | Monitor   |      1984    | Cancelled     |
| ORD201114 | C55164       | Tablet    |      1979.64 | Cancelled     |
| ORD201010 | C33729       | Monitor   |      1978.71 | Cancelled     |
| ORD201189 | C96136       | Tablet    |      1946.1  | Cancelled     |
| ORD200534 | C73289       | Chair     |      1945.77 | Cancelled     |
| ORD201128 | C49198       | Monitor   |      1940.37 | Cancelled     |
| ORD200850 | C38557       | Monitor   |      1915.5  | Cancelled     |
| ORD200058 | C60190       | Phone     |      1898.76 | Cancelled     |
| ORD200758 | C69021       | Tablet    |      1874.52 | Cancelled     |
| ORD200356 | C26966       | Printer   |      1872.9  | Cancelled     |
| ORD200344 | C95623       | Tablet    |      1870.02 | Cancelled     |
| ORD200195 | C63619       | Chair     |      1857.63 | Cancelled     |
| ORD200699 | C36813       | Laptop    |      1842.45 | Cancelled     |
| ORD200964 | C18583       | Phone     |      1822.1  | Cancelled     |
| ORD200564 | C93309       | Desk      |      1821.4  | Cancelled     |
| ORD200405 | C97774       | Monitor   |      1807.88 | Cancelled     |
| ORD200616 | C43919       | Tablet    |      1804.8  | Cancelled     |
| ORD200232 | C20731       | Printer   |      1777.76 | Cancelled     |
| ORD201028 | C60042       | Desk      |      1761.24 | Cancelled     |
| ORD200464 | C39176       | Tablet    |      1737.68 | Cancelled     |
| ORD200073 | C17269       | Monitor   |      1733.8  | Cancelled     |
| ORD200894 | C90852       | Tablet    |      1725.03 | Cancelled     |
| ORD200815 | C41320       | Printer   |      1709.52 | Cancelled     |
| ORD200599 | C28740       | Chair     |      1670.97 | Cancelled     |
| ORD200204 | C99775       | Laptop    |      1654.84 | Cancelled     |
| ORD201125 | C23555       | Desk      |      1633.44 | Cancelled     |
| ORD200818 | C25580       | Phone     |      1563.36 | Cancelled     |
| ORD200228 | C57867       | Chair     |      1543.68 | Cancelled     |
| ORD200076 | C58638       | Laptop    |      1531.52 | Cancelled     |
| ORD200682 | C50274       | Monitor   |      1528.26 | Cancelled     |
| ORD200472 | C60029       | Chair     |      1524.36 | Cancelled     |
| ORD201139 | C70659       | Chair     |      1505.46 | Cancelled     |
| ORD200130 | C29059       | Desk      |      1503.9  | Cancelled     |
| ORD200043 | C60572       | Chair     |      1497.63 | Cancelled     |
| ORD201141 | C11998       | Chair     |      1495.98 | Cancelled     |
| ORD200907 | C90898       | Desk      |      1491.95 | Cancelled     |
| ORD200636 | C60384       | Laptop    |      1484.28 | Cancelled     |
| ORD200813 | C12813       | Laptop    |      1462.7  | Cancelled     |
| ORD200056 | C54298       | Tablet    |      1437.63 | Cancelled     |
| ORD201105 | C12487       | Tablet    |      1427.07 | Cancelled     |
| ORD200966 | C58503       | Monitor   |      1402.6  | Cancelled     |
| ORD200908 | C35117       | Desk      |      1395.86 | Cancelled     |
| ORD200106 | C73514       | Desk      |      1395.15 | Cancelled     |
| ORD200198 | C37594       | Laptop    |      1361.2  | Cancelled     |
| ORD200612 | C51811       | Chair     |      1335.36 | Cancelled     |
| ORD200974 | C30722       | Desk      |      1333.9  | Cancelled     |
| ORD201196 | C20095       | Monitor   |      1325.06 | Cancelled     |
| ORD200666 | C35711       | Monitor   |      1308.48 | Cancelled     |
| ORD200355 | C18353       | Tablet    |      1299.99 | Cancelled     |
| ORD200843 | C43538       | Desk      |      1290.18 | Cancelled     |
| ORD200416 | C20881       | Laptop    |      1288.1  | Cancelled     |
| ORD200661 | C63657       | Tablet    |      1274.67 | Cancelled     |
| ORD200988 | C90318       | Desk      |      1259.12 | Cancelled     |
| ORD200775 | C73941       | Phone     |      1250.44 | Cancelled     |
| ORD200630 | C51481       | Monitor   |      1244.2  | Cancelled     |
| ORD200940 | C74003       | Printer   |      1221.28 | Cancelled     |
| ORD201151 | C94381       | Chair     |      1216.08 | Cancelled     |
| ORD201150 | C17921       | Desk      |      1210.6  | Cancelled     |
| ORD200971 | C32650       | Monitor   |      1210.52 | Cancelled     |
| ORD200133 | C87432       | Chair     |      1208.2  | Cancelled     |
| ORD200298 | C19402       | Printer   |      1204.68 | Cancelled     |
| ORD201013 | C91123       | Laptop    |      1202.24 | Cancelled     |
| ORD200948 | C94569       | Phone     |      1188.14 | Cancelled     |
| ORD200623 | C91941       | Printer   |      1188    | Cancelled     |
| ORD200116 | C47761       | Printer   |      1165.4  | Cancelled     |
| ORD201140 | C49838       | Printer   |      1105.66 | Cancelled     |
| ORD200023 | C42372       | Phone     |      1093    | Cancelled     |
| ORD200391 | C60037       | Laptop    |      1054.92 | Cancelled     |

## 7. GROUP BY + HAVING — products with more than 170 orders

```sql
SELECT Product, COUNT(*) AS OrderCount
FROM orders
GROUP BY Product
HAVING COUNT(*) > 170
ORDER BY OrderCount DESC;
```

| Product   |   OrderCount |
|:----------|-------------:|
| Printer   |          181 |
| Tablet    |          179 |
| Chair     |          178 |
| Laptop    |          173 |

## 8. Percentage contribution — each product's share of total revenue

```sql
SELECT
  Product,
  SUM(TotalPrice) AS Revenue,
  ROUND(SUM(TotalPrice) * 100.0 / (SELECT SUM(TotalPrice) FROM orders), 2) AS PctOfTotalRevenue
FROM orders
GROUP BY Product
ORDER BY Revenue DESC;
```

| Product   |   Revenue |   PctOfTotalRevenue |
|:----------|----------:|--------------------:|
| Chair     |    195620 |               15.47 |
| Printer   |    195613 |               15.47 |
| Laptop    |    192127 |               15.19 |
| Tablet    |    186569 |               14.75 |
| Monitor   |    175651 |               13.89 |
| Desk      |    167460 |               13.24 |
| Phone     |    151722 |               12    |

## 9. WHERE + LIKE — orders that used a coupon (pattern match, excludes 'NONE')

```sql
SELECT CouponCode, COUNT(*) AS TimesUsed, ROUND(AVG(TotalPrice), 2) AS AvgOrderValue
FROM orders
WHERE CouponCode != 'NONE'
GROUP BY CouponCode
ORDER BY TimesUsed DESC;
```

| CouponCode   |   TimesUsed |   AvgOrderValue |
|:-------------|------------:|----------------:|
| FREESHIP     |         313 |         1070.41 |
| WINTER15     |         292 |         1035.9  |
| SAVE10       |         286 |         1065.87 |

## 10. Order status breakdown with percentage (business health check)

```sql
SELECT
  OrderStatus,
  COUNT(*) AS OrderCount,
  ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM orders), 1) AS PctOfOrders
FROM orders
GROUP BY OrderStatus
ORDER BY OrderCount DESC;
```

| OrderStatus   |   OrderCount |   PctOfOrders |
|:--------------|-------------:|--------------:|
| Cancelled     |          250 |          20.8 |
| Returned      |          247 |          20.6 |
| Pending       |          237 |          19.8 |
| Shipped       |          235 |          19.6 |
| Delivered     |          231 |          19.3 |

## 11. Monthly revenue trend

```sql
SELECT
  strftime('%Y-%m', Date) AS Month,
  COUNT(*) AS Orders,
  SUM(TotalPrice) AS Revenue
FROM orders
GROUP BY Month
ORDER BY Month;
```

| Month   |   Orders |   Revenue |
|:--------|---------:|----------:|
| 2023-01 |       47 |   56685.8 |
| 2023-02 |       37 |   40117.7 |
| 2023-03 |       43 |   48609.4 |
| 2023-04 |       31 |   27751.7 |
| 2023-05 |       49 |   63836.8 |
| 2023-06 |       45 |   49500.2 |
| 2023-07 |       44 |   42820.7 |
| 2023-08 |       51 |   54352.1 |
| 2023-09 |       29 |   29526.7 |
| 2023-10 |       47 |   52607.8 |
| 2023-11 |       41 |   43079.7 |
| 2023-12 |       46 |   43754.7 |
| 2024-01 |       32 |   38528.1 |
| 2024-02 |       32 |   36909.6 |
| 2024-03 |       36 |   36030.9 |
| 2024-04 |       50 |   49613.1 |
| 2024-05 |       34 |   27909.1 |
| 2024-06 |       53 |   68068.5 |
| 2024-07 |       43 |   42964   |
| 2024-08 |       28 |   31991.1 |
| 2024-09 |       44 |   39795   |
| 2024-10 |       31 |   37227   |
| 2024-11 |       35 |   32413.8 |
| 2024-12 |       41 |   38785.8 |
| 2025-01 |       27 |   29099.4 |
| 2025-02 |       37 |   35317.6 |
| 2025-03 |       49 |   39200.7 |
| 2025-04 |       32 |   31821.2 |
| 2025-05 |       37 |   43396.6 |
| 2025-06 |       49 |   53047.4 |

