# Tracking Setup Documentation

**Purpose:** Document all tracking implementations  
**Updated:** As tracking is set up or changed  
**Owner:** Analytics Lead

---

## TRACKING STACK

### Analytics Platforms:
- **Google Analytics 4:** [Property ID]
- **Meta Pixel:** [Pixel ID]
- **TikTok Pixel:** [Pixel ID]

### Tag Management:
- **Google Tag Manager:** [Container ID]

### Attribution:
- **Triple Whale / Northbeam:** [Account]

---

## EVENT TRACKING

### E-commerce Events:
- ✅ PageView
- ✅ ViewContent (Product page)
- ✅ AddToCart
- ✅ InitiateCheckout
- ✅ Purchase
- ⏳ Subscribe (pending)
- ⏳ Upsell (pending)

### Custom Events:
- VSL_Started
- VSL_25%, VSL_50%, VSL_75%, VSL_Complete
- CTA_Clicked
- ExitIntent_Shown

---

## CONVERSION TRACKING

### Meta:
- Purchase event: ✅ Firing correctly
- Value passed: ✅ Yes
- Deduplicated: ✅ Yes
- CAPI enabled: ✅ Yes

### Google:
- Enhanced Ecommerce: ✅ Enabled
- Purchase event: ✅ Firing
- GA4 configured: ✅ Yes

---

## UTM STRUCTURE

**Format:** `?utm_source=[source]&utm_medium=[medium]&utm_campaign=[campaign]&utm_content=[content]`

**Example:** `?utm_source=facebook&utm_medium=paid&utm_campaign=feb_launch&utm_content=hook03_v1`

---

**Last Updated:** [Date]  
**Tracking Health:** ✅ All firing correctly
