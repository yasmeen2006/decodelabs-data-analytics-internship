-- ============================================================
-- Project 3: SQL Data Analysis — DecodeLabs Data Analytics Internship
-- Author: Yasu
-- Table: orders (1,200 rows, cleaned in Project 1)
-- ============================================================

-- 1. Basic SELECT + WHERE
-- High-value orders worth reviewing individually
SELECT OrderID, CustomerID, Product, TotalPrice, OrderStatus
FROM orders
WHERE TotalPrice > 2000
ORDER BY TotalPrice DESC;


-- 2. ORDER BY — top 10 highest-value orders overall
SELECT OrderID, Product, Quantity, UnitPrice, TotalPrice
FROM orders
ORDER BY TotalPrice DESC
LIMIT 10;


-- 3. GROUP BY + COUNT — order volume per product
SELECT Product, COUNT(*) AS OrderCount
FROM orders
GROUP BY Product
ORDER BY OrderCount DESC;


-- 4. GROUP BY + SUM — total revenue per product
SELECT Product, SUM(TotalPrice) AS TotalRevenue
FROM orders
GROUP BY Product
ORDER BY TotalRevenue DESC;


-- 5. GROUP BY + AVG — average order value per payment method
SELECT PaymentMethod, ROUND(AVG(TotalPrice), 2) AS AvgOrderValue, COUNT(*) AS Orders
FROM orders
GROUP BY PaymentMethod
ORDER BY AvgOrderValue DESC;


-- 6. WHERE with multiple conditions — cancelled orders above the overall average value
-- (subquery for the average, since HAVING only filters aggregated groups, not raw rows)
SELECT OrderID, CustomerID, Product, TotalPrice, OrderStatus
FROM orders
WHERE OrderStatus = 'Cancelled'
  AND TotalPrice > (SELECT AVG(TotalPrice) FROM orders)
ORDER BY TotalPrice DESC;


-- 7. GROUP BY + HAVING — products with more than 170 orders
-- (HAVING filters the grouped/aggregated result, unlike WHERE which filters raw rows)
SELECT Product, COUNT(*) AS OrderCount
FROM orders
GROUP BY Product
HAVING COUNT(*) > 170
ORDER BY OrderCount DESC;


-- 8. Percentage contribution — each product's share of total revenue
SELECT
  Product,
  SUM(TotalPrice) AS Revenue,
  ROUND(SUM(TotalPrice) * 100.0 / (SELECT SUM(TotalPrice) FROM orders), 2) AS PctOfTotalRevenue
FROM orders
GROUP BY Product
ORDER BY Revenue DESC;


-- 9. WHERE + LIKE — orders that used a coupon (pattern match, excludes 'NONE')
SELECT CouponCode, COUNT(*) AS TimesUsed, ROUND(AVG(TotalPrice), 2) AS AvgOrderValue
FROM orders
WHERE CouponCode != 'NONE'
GROUP BY CouponCode
ORDER BY TimesUsed DESC;


-- 10. Order status breakdown with percentage (business health check)
SELECT
  OrderStatus,
  COUNT(*) AS OrderCount,
  ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM orders), 1) AS PctOfOrders
FROM orders
GROUP BY OrderStatus
ORDER BY OrderCount DESC;


-- 11. Monthly revenue trend
SELECT
  strftime('%Y-%m', Date) AS Month,
  COUNT(*) AS Orders,
  SUM(TotalPrice) AS Revenue
FROM orders
GROUP BY Month
ORDER BY Month;
