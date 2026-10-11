# generate_unslopped_hub.py
"""
AutoML & MBR Research Hub — Literature & Knowledge Tree Showcase Generator
Generates index.html with a high-taste Card Grid Library layout adhering to:
- Poteto Mode & Taste Skill (Anti-AI slop, zero lilac/neon glow, Geist typography, Warm Charcoal & Terracotta Red palette)
- ASD-STE100 & Humanizer writing standards
- 100% SVG primitives (zero emojis)
- Complete mobile stability & viewport optimization (100dvh full-screen modal, swipeable chips, 0px min-width search)
- Tab 1: 30 bài chọn lọc (MBR & ML) with prominent PID badges ([M018], [M002], etc.)
- Tab 2: Tài liệu tham khảo (65 bài) with lightning-fast responsive table/list and direct dual PDF links
"""

import json
import html

# Load master catalogs
with open('branche_v2/papers_catalog.json', 'r', encoding='utf-8') as f:
    catalog_30 = json.load(f)

with open('branche_v2/extended_catalog.json', 'r', encoding='utf-8') as f:
    extended_65 = json.load(f)

catalog_json_str = json.dumps(catalog_30, ensure_ascii=False, indent=2)
extended_json_str = json.dumps(extended_65, ensure_ascii=False, indent=2)

html_template = f'''<!DOCTYPE html>
<html lang="vi" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
  <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
  <meta http-equiv="Pragma" content="no-cache">
  <meta http-equiv="Expires" content="0">
  <title>AutoML & MBR Research Hub — Thư Viện Tri Thức & Công Nghệ Màng</title>
  
  <!-- Typography: Geist & Geist Mono -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700;800&family=Geist+Mono:wght@400;500;600&display=swap" rel="stylesheet">
  
  <!-- Markdown & KaTeX Math Rendering Engines -->
  <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
  <script src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js"></script>

  <style>
    /* CSS Variables: Warm Charcoal & Terracotta Red (Reference Mockup Standard) */
    :root {{
      --bg: #141312;
      --surface: #1a1816;
      --surface-elevated: #22201d;
      --surface-hover: #2c2925;
      --card-bg: #1c1a18;
      --card-border: rgba(255, 255, 255, 0.08);
      --card-border-hover: rgba(220, 38, 38, 0.5);
      --sunken-bg: #121110;
      --sunken-border: rgba(255, 255, 255, 0.06);
      --border: rgba(255, 255, 255, 0.08);
      --border-subtle: rgba(255, 255, 255, 0.04);
      --border-strong: rgba(255, 255, 255, 0.16);
      --text: #f5f5f4;
      --text-muted: #a8a29e;
      --text-faint: #78716c;
      --text-secondary: #d6d3d1;
      
      /* Primary Terracotta Red (CTA Buttons & Active Filter Chips) */
      --primary: #c53030;
      --primary-rgb: 197, 48, 48;
      --primary-hover: #b91c1c;
      --primary-bg: rgba(197, 48, 48, 0.15);
      --primary-border: rgba(197, 48, 48, 0.4);

      /* Subtitle / Tagline Terracotta Accent */
      --subtitle: #ea580c;
      
      /* Category Color Tokens */
      --accent-amber: #f59e0b;
      --accent-amber-bg: rgba(245, 158, 11, 0.1);
      --accent-amber-border: rgba(245, 158, 11, 0.3);

      --accent-bio: #10b981;
      --accent-bio-bg: rgba(16, 185, 129, 0.1);
      --accent-bio-border: rgba(16, 185, 129, 0.3);

      --accent-terracotta: #f97316;
      --accent-terracotta-bg: rgba(249, 115, 22, 0.1);
      --accent-terracotta-border: rgba(249, 115, 22, 0.3);
      
      --accent-stone: #a8a29e;
      --accent-stone-bg: rgba(168, 162, 158, 0.1);
      --accent-stone-border: rgba(168, 162, 158, 0.3);

      --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.45);
      --shadow-md: 0 6px 20px -3px rgba(0, 0, 0, 0.55);
      --shadow-lg: 0 20px 48px -10px rgba(0, 0, 0, 0.75);
      --radius-sm: 6px;
      --radius-md: 10px;
      --radius-lg: 14px;
      --radius-xl: 16px;
      --transition: 0.18s cubic-bezier(0.16, 1, 0.3, 1);
    }}

    [data-theme="light"] {{
      --bg: #faf8f5;
      --surface: #ffffff;
      --surface-elevated: #f4efe6;
      --surface-hover: #ebe4d8;
      --card-bg: #ffffff;
      --card-border: #e7e1d4;
      --card-border-hover: #c53030;
      --sunken-bg: #f4efe6;
      --sunken-border: #e7e1d4;
      --border: #e7e1d4;
      --border-subtle: rgba(0, 0, 0, 0.04);
      --border-strong: #d3cbbe;
      --text: #1c1917;
      --text-muted: #78716c;
      --text-faint: #a8a29e;
      --text-secondary: #44403c;
      
      --primary: #c53030;
      --primary-rgb: 197, 48, 48;
      --primary-hover: #991b1b;
      --primary-bg: #fef2f2;
      --primary-border: rgba(197, 48, 48, 0.3);

      --subtitle: #c2410c;
      
      --accent-amber: #b45309;
      --accent-amber-bg: rgba(245, 158, 11, 0.12);
      --accent-amber-border: rgba(180, 83, 9, 0.3);

      --accent-bio: #047857;
      --accent-bio-bg: rgba(16, 185, 129, 0.12);
      --accent-bio-border: rgba(4, 120, 87, 0.3);

      --accent-terracotta: #c2410c;
      --accent-terracotta-bg: rgba(249, 115, 22, 0.12);
      --accent-terracotta-border: rgba(194, 65, 12, 0.3);
      
      --accent-stone: #57534e;
      --accent-stone-bg: rgba(168, 162, 158, 0.15);
      --accent-stone-border: rgba(87, 83, 78, 0.3);

      --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
      --shadow-md: 0 4px 16px -2px rgba(0, 0, 0, 0.08);
      --shadow-lg: 0 16px 36px -8px rgba(0, 0, 0, 0.14);
    }}

    /* Global Box-Sizing and Anti-Wobble Core */
    *, *::before, *::after {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}
    
    html, body {{
      overflow-x: hidden;
      width: 100%;
      max-width: 100vw;
      font-family: "Geist", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      background-color: var(--bg);
      color: var(--text);
      line-height: 1.5;
      min-height: 100dvh;
      -webkit-font-smoothing: antialiased;
    }}

    /* SVG Icon Primitives */
    .icon {{
      display: inline-block;
      width: 16px;
      height: 16px;
      stroke-width: 1.8;
      stroke: currentColor;
      fill: none;
      stroke-linecap: round;
      stroke-linejoin: round;
      flex-shrink: 0;
      vertical-align: middle;
    }}
    .icon-xs {{ width: 12px; height: 12px; }}
    .icon-sm {{ width: 14px; height: 14px; }}
    .icon-md {{ width: 16px; height: 16px; }}
    .icon-lg {{ width: 20px; height: 20px; }}

    /* Top Sticky Navigation Header */
    header {{
      background: var(--surface);
      border-bottom: 1px solid var(--border);
      padding: 0 24px;
      height: 56px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      position: sticky;
      top: 0;
      z-index: 40;
    }}

    .brand-wrap {{
      display: flex;
      align-items: center;
      gap: 12px;
      min-width: 0;
    }}

    .brand-logo-badge {{
      width: 32px;
      height: 32px;
      border-radius: var(--radius-sm);
      background: var(--surface-elevated);
      border: 1px solid var(--border-strong);
      display: flex;
      align-items: center;
      justify-content: center;
      color: var(--primary);
      flex-shrink: 0;
    }}

    .brand-title-wrap {{
      display: flex;
      align-items: baseline;
      gap: 8px;
      min-width: 0;
      overflow: hidden;
    }}

    .brand-title {{
      font-size: 15px;
      font-weight: 700;
      letter-spacing: -0.025em;
      color: var(--text);
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }}

    .brand-tag {{
      font-size: 11px;
      font-weight: 600;
      padding: 2px 7px;
      border-radius: 4px;
      background: var(--primary-bg);
      color: #ef4444;
      border: 1px solid var(--primary-border);
      font-family: "Geist Mono", monospace;
      white-space: nowrap;
    }}
    [data-theme="light"] .brand-tag {{
      color: var(--primary);
    }}

    /* Global Statistics Bar */
    .stats-pills {{
      display: flex;
      gap: 8px;
      align-items: center;
    }}

    .stat-pill {{
      font-size: 12px;
      color: var(--text-muted);
      background: var(--surface-elevated);
      border: 1px solid var(--border);
      padding: 4px 10px;
      border-radius: var(--radius-sm);
      display: flex;
      align-items: center;
      gap: 6px;
      font-variant-numeric: tabular-nums;
      white-space: nowrap;
    }}
    .stat-pill strong {{ color: var(--text); font-weight: 600; }}

    .nav-actions {{
      display: flex;
      align-items: center;
      gap: 8px;
      flex-shrink: 0;
    }}

    .btn-action {{
      background: var(--surface-elevated);
      border: 1px solid var(--border);
      color: var(--text);
      padding: 6px 12px;
      border-radius: var(--radius-sm);
      font-size: 12.5px;
      font-weight: 500;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      text-decoration: none;
      transition: background var(--transition), border-color var(--transition), color var(--transition);
      user-select: none;
      white-space: nowrap;
    }}
    .btn-action:hover {{
      background: var(--surface-hover);
      border-color: var(--border-strong);
      color: #ef4444;
    }}
    [data-theme="light"] .btn-action:hover {{
      color: var(--primary);
    }}
    .btn-action:active {{ transform: scale(0.98); }}

    /* Main Showcase Container */
    main.library-main {{
      flex: 1;
      max-width: 1440px;
      width: 100%;
      margin: 0 auto;
      padding: 24px 24px 60px 24px;
      display: flex;
      flex-direction: column;
      gap: 20px;
    }}

    /* Main Hub Navigation Tabs (Tab 1 & Tab 2) */
    .hub-main-tabs {{
      display: flex;
      align-items: center;
      gap: 10px;
      border-bottom: 1px solid var(--border);
      padding-bottom: 12px;
      overflow-x: auto;
      -webkit-overflow-scrolling: touch;
      scrollbar-width: none;
      width: 100%;
    }}
    .hub-main-tabs::-webkit-scrollbar {{ display: none; }}

    .hub-tab-btn {{
      background: var(--surface-elevated);
      border: 1px solid var(--border);
      color: var(--text-muted);
      font-size: 14px;
      font-weight: 600;
      padding: 9px 18px;
      border-radius: var(--radius-md);
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      transition: all var(--transition);
      white-space: nowrap;
      flex-shrink: 0;
      user-select: none;
    }}
    .hub-tab-btn:hover {{
      background: var(--surface-hover);
      color: var(--text);
      border-color: var(--border-strong);
    }}
    .hub-tab-btn.active {{
      background: var(--primary);
      color: #ffffff;
      border-color: var(--primary);
      box-shadow: 0 2px 10px rgba(var(--primary-rgb), 0.35);
    }}

    /* Tab Content Panes */
    .hub-pane {{
      display: none;
      width: 100%;
      flex-direction: column;
      gap: 20px;
    }}
    .hub-pane.active {{
      display: flex;
    }}

    /* Control Toolbar (Search, Filter Chips, View Toggle) */
    .library-toolbar {{
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: var(--radius-xl);
      padding: 14px 18px;
      display: flex;
      flex-direction: column;
      gap: 14px;
      box-shadow: var(--shadow-sm);
      width: 100%;
    }}

    .toolbar-row {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      width: 100%;
    }}

    .search-input-wrap {{
      position: relative;
      flex: 1;
      min-width: 0;
      width: 100%;
    }}

    .search-input-wrap input {{
      width: 100%;
      background: var(--bg);
      border: 1px solid var(--border);
      color: var(--text);
      font-size: 13.5px;
      font-family: inherit;
      padding: 9px 12px 9px 38px;
      border-radius: var(--radius-md);
      outline: none;
      transition: border-color var(--transition), box-shadow var(--transition);
    }}
    .search-input-wrap input:focus {{
      border-color: var(--primary);
      box-shadow: 0 0 0 3px rgba(var(--primary-rgb), 0.18);
    }}

    .search-icon-pos {{
      position: absolute;
      left: 12px;
      top: 50%;
      transform: translateY(-50%);
      color: var(--text-faint);
      pointer-events: none;
    }}

    .search-clear-btn {{
      position: absolute;
      right: 10px;
      top: 50%;
      transform: translateY(-50%);
      background: none;
      border: none;
      color: var(--text-faint);
      cursor: pointer;
      display: none;
      padding: 3px;
    }}
    .search-clear-btn.active {{ display: block; }}
    .search-clear-btn:hover {{ color: var(--text); }}

    /* Filter Chips Row */
    .filter-chips-row {{
      display: flex;
      align-items: center;
      gap: 8px;
      flex-wrap: wrap;
      width: 100%;
    }}

    .filter-chip {{
      background: var(--surface-elevated);
      border: 1px solid var(--border);
      color: var(--text-muted);
      font-size: 12.5px;
      font-weight: 500;
      padding: 6px 14px;
      border-radius: 9999px;
      cursor: pointer;
      user-select: none;
      transition: all var(--transition);
      display: inline-flex;
      align-items: center;
      gap: 6px;
      flex-shrink: 0;
      white-space: nowrap;
    }}
    .filter-chip:hover {{
      background: var(--surface-hover);
      color: var(--text);
      border-color: var(--border-strong);
    }}
    .filter-chip.active {{
      background: var(--primary);
      color: #ffffff;
      border-color: var(--primary);
      font-weight: 600;
      box-shadow: 0 2px 8px rgba(var(--primary-rgb), 0.35);
    }}

    .filter-chip-count {{
      font-family: "Geist Mono", monospace;
      font-size: 11px;
      opacity: 0.85;
      padding: 1px 5px;
      background: rgba(0, 0, 0, 0.2);
      border-radius: 9999px;
    }}

    /* View Switcher */
    .view-switcher {{
      display: flex;
      background: var(--bg);
      border: 1px solid var(--border);
      border-radius: var(--radius-sm);
      padding: 3px;
      gap: 2px;
      flex-shrink: 0;
    }}

    .btn-view-toggle {{
      background: transparent;
      border: none;
      color: var(--text-muted);
      padding: 5px 10px;
      border-radius: 4px;
      font-size: 12px;
      font-weight: 600;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 5px;
      transition: all var(--transition);
      white-space: nowrap;
    }}
    .btn-view-toggle:hover {{ color: var(--text); }}
    .btn-view-toggle.active {{
      background: var(--surface-elevated);
      color: #ef4444;
      box-shadow: var(--shadow-sm);
    }}
    [data-theme="light"] .btn-view-toggle.active {{
      color: var(--primary);
    }}

    /* Results Indicator */
    .results-count-bar {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      font-size: 12.5px;
      color: var(--text-faint);
      padding: 0 4px;
      flex-wrap: wrap;
      gap: 8px;
    }}

    /* Card Grid Layout */
    .research-grid {{
      display: grid;
      grid-template-columns: repeat(3, minmax(0, 1fr));
      gap: 24px;
      width: 100%;
    }}

    /* Research Card */
    .research-card {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: var(--radius-lg);
      padding: 20px 22px;
      display: flex;
      flex-direction: column;
      box-shadow: var(--shadow-sm);
      transition: transform 0.2s cubic-bezier(0.16, 1, 0.3, 1), border-color 0.2s ease, box-shadow 0.2s ease;
      position: relative;
    }}
    .research-card:hover {{
      transform: translateY(-3px);
      border-color: var(--card-border-hover);
      box-shadow: var(--shadow-md), 0 0 0 1px rgba(var(--primary-rgb), 0.25);
    }}

    /* Card Row 1: Category Tag & Monospace Year/Slug */
    .card-row-meta {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 8px;
      margin-bottom: 12px;
      flex-wrap: wrap;
    }}

    .card-meta-left {{
      display: flex;
      align-items: center;
      gap: 6px;
      flex-wrap: wrap;
    }}

    /* Prominent PID Badge */
    .pid-badge {{
      font-family: "Geist Mono", monospace;
      font-size: 11px;
      font-weight: 700;
      color: #ef4444;
      background: rgba(239, 68, 68, 0.12);
      border: 1px solid rgba(239, 68, 68, 0.35);
      padding: 2px 7px;
      border-radius: var(--radius-sm);
      letter-spacing: 0.04em;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
    }}
    [data-theme="light"] .pid-badge {{
      color: #b91c1c;
      background: rgba(185, 28, 28, 0.1);
      border-color: rgba(185, 28, 28, 0.3);
    }}

    .category-tag {{
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.04em;
      padding: 2.5px 8px;
      border-radius: 4px;
      font-family: "Geist", sans-serif;
      transition: all var(--transition);
      white-space: nowrap;
    }}
    
    /* Dark Mode Category Badges */
    .category-tag.theme-amber,
    .category-tag.theme-automl {{
      background: rgba(245, 158, 11, 0.1);
      color: #f59e0b;
      border: 1px solid rgba(245, 158, 11, 0.3);
    }}
    .category-tag.theme-emerald,
    .category-tag.theme-mbr,
    .category-tag.theme-teal {{
      background: rgba(16, 185, 129, 0.1);
      color: #10b981;
      border: 1px solid rgba(16, 185, 129, 0.3);
    }}
    .category-tag.theme-terracotta,
    .category-tag.theme-anammox,
    .category-tag.theme-orange,
    .category-tag.theme-transfer {{
      background: rgba(249, 115, 22, 0.1);
      color: #f97316;
      border: 1px solid rgba(249, 115, 22, 0.3);
    }}
    .category-tag.theme-stone,
    .category-tag.theme-slate,
    .category-tag.theme-review,
    .category-tag.theme-water_quality {{
      background: rgba(168, 162, 158, 0.1);
      color: #a8a29e;
      border: 1px solid rgba(168, 162, 158, 0.3);
    }}

    /* Light Mode Category Badges */
    [data-theme="light"] .category-tag.theme-amber,
    [data-theme="light"] .category-tag.theme-automl {{
      background: rgba(245, 158, 11, 0.12);
      color: #b45309;
      border: 1px solid rgba(180, 83, 9, 0.3);
    }}
    [data-theme="light"] .category-tag.theme-emerald,
    [data-theme="light"] .category-tag.theme-mbr,
    [data-theme="light"] .category-tag.theme-teal {{
      background: rgba(16, 185, 129, 0.12);
      color: #047857;
      border: 1px solid rgba(4, 120, 87, 0.3);
    }}
    [data-theme="light"] .category-tag.theme-terracotta,
    [data-theme="light"] .category-tag.theme-anammox,
    [data-theme="light"] .category-tag.theme-orange,
    [data-theme="light"] .category-tag.theme-transfer {{
      background: rgba(249, 115, 22, 0.12);
      color: #c2410c;
      border: 1px solid rgba(194, 65, 12, 0.3);
    }}
    [data-theme="light"] .category-tag.theme-stone,
    [data-theme="light"] .category-tag.theme-slate,
    [data-theme="light"] .category-tag.theme-review,
    [data-theme="light"] .category-tag.theme-water_quality {{
      background: rgba(168, 162, 158, 0.15);
      color: #57534e;
      border: 1px solid rgba(87, 83, 78, 0.3);
    }}

    /* Paper Number Badge */
    .paper-num-badge {{
      font-family: "Geist Mono", monospace;
      font-size: 11px;
      font-weight: 700;
      color: #ea580c;
      background: rgba(234, 88, 12, 0.12);
      border: 1px solid rgba(234, 88, 12, 0.35);
      padding: 2px 7px;
      border-radius: var(--radius-sm);
      letter-spacing: 0.04em;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
    }}
    [data-theme="light"] .paper-num-badge {{
      color: #c2410c;
      background: rgba(194, 65, 12, 0.1);
      border-color: rgba(194, 65, 12, 0.3);
    }}

    .card-id-slug {{
      font-family: "Geist Mono", monospace;
      font-size: 11.5px;
      color: var(--text-faint);
      display: flex;
      align-items: center;
      gap: 5px;
      margin-left: auto;
      white-space: nowrap;
    }}

    /* Card Title */
    .card-title {{
      font-size: 15.5px;
      font-weight: 700;
      line-height: 1.38;
      letter-spacing: -0.02em;
      color: var(--text);
      margin-bottom: 6px;
      cursor: pointer;
      transition: color var(--transition);
      display: -webkit-box;
      -webkit-line-clamp: 2;
      -webkit-box-orient: vertical;
      overflow: hidden;
      word-break: break-word;
    }}
    .card-title:hover {{ color: #ef4444; }}
    [data-theme="light"] .card-title:hover {{ color: var(--primary); }}

    /* Technical Subtitle */
    .card-subtitle {{
      font-size: 12.5px;
      font-weight: 600;
      color: var(--subtitle);
      line-height: 1.4;
      margin-bottom: 10px;
      display: -webkit-box;
      -webkit-line-clamp: 1;
      -webkit-box-orient: vertical;
      overflow: hidden;
    }}
    [data-theme="light"] .card-subtitle {{ color: var(--subtitle); }}

    /* Source Citation */
    .card-source {{
      font-size: 12px;
      color: var(--text-muted);
      display: flex;
      align-items: center;
      gap: 6px;
      margin-bottom: 12px;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }}

    /* Narrative Description */
    .card-desc {{
      font-size: 13px;
      color: var(--text-muted);
      line-height: 1.55;
      margin-bottom: 16px;
      display: -webkit-box;
      -webkit-line-clamp: 3;
      -webkit-box-orient: vertical;
      overflow: hidden;
      flex-grow: 1;
    }}

    /* Quantitative Lineage Metrics */
    .sunken-metrics {{
      background: var(--sunken-bg);
      border: 1px solid var(--sunken-border);
      border-radius: var(--radius-sm);
      padding: 8px 12px;
      display: flex;
      align-items: center;
      justify-content: space-around;
      gap: 12px;
      font-size: 11.5px;
      color: var(--text-muted);
      margin-bottom: 16px;
      flex-wrap: wrap;
    }}
    .sunken-metrics strong {{
      font-family: "Geist Mono", monospace;
      color: var(--text);
      font-weight: 700;
    }}
    .sunken-dot {{
      color: var(--border-strong);
      font-size: 10px;
    }}

    /* Card Action Footer */
    .card-actions {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 8px;
      margin-top: auto;
      padding-top: 12px;
      border-top: 1px solid var(--border-subtle);
    }}

    .btn-primary-card {{
      background: var(--primary);
      color: #ffffff;
      border: 1px solid var(--primary);
      border-radius: var(--radius-sm);
      padding: 7px 14px;
      font-size: 12.5px;
      font-weight: 600;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: background var(--transition), transform var(--transition);
      box-shadow: 0 1px 3px rgba(var(--primary-rgb), 0.35);
      user-select: none;
      white-space: nowrap;
    }}
    .btn-primary-card:hover {{
      background: var(--primary-hover);
      transform: translateY(-1px);
    }}
    .btn-primary-card:active {{ transform: translateY(0); }}

    .btn-secondary-card {{
      background: var(--surface-elevated);
      border: 1px solid var(--border);
      color: var(--text);
      border-radius: var(--radius-sm);
      padding: 7px 12px;
      font-size: 12.5px;
      font-weight: 500;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all var(--transition);
      user-select: none;
      text-decoration: none;
      white-space: nowrap;
    }}
    .btn-secondary-card:hover {{
      background: var(--surface-hover);
      border-color: var(--border-strong);
      color: #ef4444;
    }}
    [data-theme="light"] .btn-secondary-card:hover {{
      color: var(--primary);
    }}

    .btn-pdf-badge {{
      background: var(--accent-bio-bg);
      border: 1px solid var(--accent-bio-border);
      color: var(--accent-bio);
      border-radius: var(--radius-sm);
      padding: 6px 10px;
      font-size: 12px;
      font-weight: 600;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 5px;
      transition: all var(--transition);
      white-space: nowrap;
    }}
    .btn-pdf-badge:hover {{
      background: rgba(16, 185, 129, 0.22);
      transform: translateY(-1px);
    }}

    /* List View (Table Variant of Tab 1) */
    .research-grid.list-view {{
      grid-template-columns: 1fr;
      gap: 12px;
    }}
    .research-grid.list-view .research-card {{
      flex-direction: row;
      align-items: center;
      gap: 16px;
      padding: 14px 18px;
    }}
    .research-grid.list-view .card-row-meta {{
      margin-bottom: 0;
      flex: 0 0 180px;
    }}
    .research-grid.list-view .card-title {{
      margin-bottom: 2px;
      font-size: 14px;
      flex: 1;
    }}
    .research-grid.list-view .card-subtitle,
    .research-grid.list-view .card-desc,
    .research-grid.list-view .sunken-metrics {{
      display: none;
    }}

    /* Tab 2: Lightweight Extended Catalog Table */
    .extended-container {{
      width: 100%;
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: var(--radius-xl);
      padding: 18px;
      display: flex;
      flex-direction: column;
      gap: 16px;
      box-shadow: var(--shadow-sm);
    }}

    .extended-header-row {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      flex-wrap: wrap;
    }}

    .extended-info-badge {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      font-size: 13px;
      color: var(--text-muted);
    }}
    .extended-info-badge strong {{
      color: var(--text);
    }}

    .extended-table-wrap {{
      width: 100%;
      overflow-x: auto;
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      background: var(--card-bg);
      -webkit-overflow-scrolling: touch;
    }}

    .extended-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 13px;
      text-align: left;
    }}

    .extended-table th {{
      background: var(--surface-elevated);
      color: var(--text-muted);
      font-size: 11.5px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.04em;
      padding: 12px 14px;
      border-bottom: 1px solid var(--border);
      white-space: nowrap;
    }}

    .extended-table td {{
      padding: 12px 14px;
      border-bottom: 1px solid var(--border-subtle);
      vertical-align: middle;
      color: var(--text-secondary);
    }}

    .extended-table tr:hover td {{
      background: var(--surface-hover);
    }}

    .ext-title-col {{
      min-width: 280px;
    }}
    .ext-title-vn {{
      font-weight: 600;
      color: var(--text);
      line-height: 1.4;
      margin-bottom: 3px;
    }}
    .ext-title-en {{
      font-size: 11.5px;
      color: var(--text-muted);
      font-style: italic;
      line-height: 1.35;
    }}
    .ext-meta-sub {{
      font-size: 11.5px;
      color: var(--text-faint);
      margin-top: 2px;
    }}

    /* Detail Modal Reader (Experience First) */
    .reader-modal-overlay {{
      position: fixed;
      inset: 0;
      background: rgba(14, 13, 12, 0.88);
      backdrop-filter: blur(12px);
      z-index: 100;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 18px;
    }}
    .reader-modal-overlay.active {{
      display: flex;
      animation: modalFadeIn 0.2s cubic-bezier(0.16, 1, 0.3, 1);
    }}

    @keyframes modalFadeIn {{
      from {{ opacity: 0; transform: scale(0.99); }}
      to {{ opacity: 1; transform: scale(1); }}
    }}

    .reader-modal-box {{
      width: 96vw;
      max-width: 1540px;
      height: 92vh;
      background: var(--surface);
      border: 1px solid var(--border-strong);
      border-radius: var(--radius-xl);
      box-shadow: var(--shadow-lg);
      display: flex;
      flex-direction: column;
      overflow: hidden;
      position: relative;
    }}

    /* Modal Header */
    .modal-header {{
      background: var(--surface);
      border-bottom: 1px solid var(--border);
      padding: 14px 20px;
      display: flex;
      flex-direction: column;
      gap: 12px;
      flex-shrink: 0;
    }}

    .modal-header-top {{
      display: flex;
      align-items: flex-start;
      justify-content: space-between;
      gap: 16px;
    }}

    .modal-title-col {{
      flex: 1;
      min-width: 0;
      display: flex;
      flex-direction: column;
      gap: 4px;
    }}

    .modal-meta-row {{
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 12px;
      color: var(--text-muted);
      flex-wrap: wrap;
    }}

    .modal-paper-title {{
      font-size: 16px;
      font-weight: 700;
      line-height: 1.35;
      color: var(--text);
      letter-spacing: -0.02em;
    }}

    .modal-paper-subtitle {{
      font-size: 13px;
      font-weight: 600;
      color: var(--subtitle);
    }}

    .modal-actions-group {{
      display: flex;
      align-items: center;
      gap: 8px;
      flex-shrink: 0;
    }}

    /* Direct PDF buttons in modal */
    .btn-pdf {{
      background: var(--surface-elevated);
      border: 1px solid var(--border-strong);
      color: var(--text);
      padding: 6px 12px;
      border-radius: var(--radius-sm);
      font-size: 12px;
      font-weight: 600;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all var(--transition);
      user-select: none;
      white-space: nowrap;
    }}
    .btn-pdf:hover {{
      background: var(--surface-hover);
      border-color: var(--primary);
      color: #ef4444;
      transform: translateY(-1px);
    }}
    [data-theme="light"] .btn-pdf:hover {{
      color: var(--primary);
    }}
    .btn-pdf.bilingual {{
      background: var(--accent-bio-bg);
      border-color: var(--accent-bio-border);
      color: var(--accent-bio);
    }}
    .btn-pdf.bilingual:hover {{
      background: rgba(16, 185, 129, 0.22);
    }}
    .btn-pdf.disabled {{
      opacity: 0.45;
      pointer-events: none;
      border-color: var(--border-subtle);
      color: var(--text-faint);
    }}

    .btn-close-modal {{
      background: var(--surface-elevated);
      border: 1px solid var(--border);
      color: var(--text-muted);
      width: 32px;
      height: 32px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      transition: all var(--transition);
      flex-shrink: 0;
    }}
    .btn-close-modal:hover {{
      background: var(--surface-hover);
      color: var(--text);
      border-color: var(--border-strong);
      transform: scale(1.05);
    }}

    /* Modal Navigation Bar: 4 Tabs + Utilities */
    .modal-nav-row {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      flex-wrap: wrap;
    }}

    .modal-view-tabs {{
      display: flex;
      background: var(--bg);
      border: 1px solid var(--border);
      border-radius: var(--radius-sm);
      padding: 3px;
      gap: 2px;
    }}

    .modal-tab-btn {{
      background: transparent;
      border: none;
      color: var(--text-muted);
      font-size: 12.5px;
      font-weight: 600;
      padding: 6px 14px;
      border-radius: 4px;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all var(--transition);
      white-space: nowrap;
    }}
    .modal-tab-btn:hover {{ color: var(--text); }}
    .modal-tab-btn.active {{
      background: var(--surface-elevated);
      color: #ef4444;
      box-shadow: var(--shadow-sm);
    }}
    [data-theme="light"] .modal-tab-btn.active {{
      color: var(--primary);
    }}

    .modal-utility-group {{
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    /* Modal Panes Body */
    .modal-body {{
      flex: 1;
      position: relative;
      overflow: hidden;
      display: flex;
      flex-direction: column;
    }}

    .modal-pane {{
      position: absolute;
      inset: 0;
      display: none;
      overflow: hidden;
      flex-direction: column;
    }}
    .modal-pane.active {{ display: flex; }}

    /* Pane 1: Mindmap Frame & Mobile Touch Control */
    .mindmap-touch-bar {{
      display: none;
      background: var(--surface-elevated);
      border-bottom: 1px solid var(--border);
      padding: 6px 12px;
      align-items: center;
      justify-content: space-between;
      font-size: 11.5px;
      color: var(--text-muted);
      gap: 8px;
    }}
    .btn-touch-toggle {{
      background: var(--surface);
      border: 1px solid var(--border-strong);
      color: var(--text);
      padding: 4px 10px;
      border-radius: 4px;
      font-size: 11px;
      font-weight: 600;
      cursor: pointer;
    }}
    .mindmap-frame {{
      width: 100%;
      height: 100%;
      border: none;
      background: var(--bg);
      flex: 1;
    }}

    /* Pane 2: Knowledge Tree Markdown Layout */
    .tree-layout {{
      display: flex;
      width: 100%;
      height: 100%;
      overflow: hidden;
    }}

    .tree-article-wrap {{
      flex: 1;
      height: 100%;
      overflow-y: auto;
      padding: 24px 32px 60px 32px;
      background: var(--bg);
      scroll-behavior: smooth;
    }}

    .tree-article-inner {{
      max-width: 860px;
      margin: 0 auto;
      line-height: 1.7;
      color: var(--text-secondary);
      font-size: 14.5px;
    }}

    .tree-article-inner h1 {{
      font-size: 22px;
      font-weight: 800;
      color: var(--text);
      margin: 28px 0 14px 0;
      letter-spacing: -0.02em;
    }}
    .tree-article-inner h2 {{
      font-size: 17px;
      font-weight: 700;
      color: var(--text);
      margin: 24px 0 12px 0;
      padding-bottom: 6px;
      border-bottom: 1px solid var(--border);
    }}
    .tree-article-inner h3 {{
      font-size: 15px;
      font-weight: 600;
      color: #ef4444;
      margin: 18px 0 8px 0;
    }}
    [data-theme="light"] .tree-article-inner h3 {{
      color: var(--primary);
    }}
    .tree-article-inner p {{
      margin-bottom: 12px;
      color: var(--text);
      font-size: 14px;
    }}
    .tree-article-inner ul {{
      margin-bottom: 14px;
      padding-left: 20px;
    }}
    .tree-article-inner li {{
      margin-bottom: 5px;
      color: var(--text);
      font-size: 13.5px;
    }}
    .tree-article-inner img {{
      max-width: 100%;
      border-radius: var(--radius-sm);
      border: 1px solid var(--border);
      margin: 14px 0;
      background: #141312;
    }}
    [data-theme="light"] .tree-article-inner img {{
      background: #f4efe6;
    }}
    .tree-article-inner table {{
      width: 100%;
      border-collapse: collapse;
      margin: 16px 0;
      font-size: 13px;
    }}
    .tree-article-inner th, .tree-article-inner td {{
      border: 1px solid var(--border);
      padding: 8px 12px;
      text-align: left;
    }}
    .tree-article-inner th {{
      background: var(--surface-elevated);
      font-weight: 600;
    }}

    .tree-toc-sidebar {{
      width: 270px;
      border-left: 1px solid var(--border);
      background: var(--surface);
      overflow-y: auto;
      padding: 16px 14px;
      font-size: 12px;
      flex-shrink: 0;
    }}
    .tree-toc-title {{
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--text-faint);
      margin-bottom: 10px;
      display: flex;
      align-items: center;
      gap: 6px;
    }}
    .toc-item {{
      display: block;
      color: var(--text-muted);
      text-decoration: none;
      padding: 4px 6px;
      border-radius: var(--radius-sm);
      margin-bottom: 2px;
      line-height: 1.35;
      overflow: hidden;
      text-overflow: ellipsis;
      white-space: nowrap;
      transition: color var(--transition), background var(--transition);
    }}
    .toc-item:hover {{
      color: #ef4444;
      background: var(--surface-hover);
    }}
    [data-theme="light"] .toc-item:hover {{
      color: var(--primary);
    }}
    .toc-item.level-3 {{
      padding-left: 14px;
      font-size: 11.5px;
      color: var(--text-faint);
    }}

    /* Notice for In-Progress Trees (L-01, L-02, L-03) */
    .tree-in-progress-notice {{
      background: var(--card-bg);
      border: 1px solid var(--border-strong);
      border-radius: var(--radius-md);
      padding: 24px;
      margin: 20px auto;
      max-width: 650px;
      text-align: center;
    }}
    .tree-in-progress-notice h3 {{
      color: #ea580c;
      font-size: 16px;
      margin-bottom: 10px;
    }}
    .tree-in-progress-notice p {{
      color: var(--text-muted);
      font-size: 13.5px;
      line-height: 1.6;
      margin-bottom: 14px;
    }}

    /* Tab 3: Figures & Tables Gallery */
    .gallery-pane-wrap {{
      width: 100%;
      height: 100%;
      overflow-y: auto;
      padding: 24px;
    }}
    .gallery-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(340px, 1fr));
      gap: 18px;
      max-width: 1400px;
      margin: 0 auto;
    }}
    .fig-card {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: var(--radius-md);
      overflow: hidden;
      display: flex;
      flex-direction: column;
      box-shadow: var(--shadow-sm);
      cursor: pointer;
      transition: transform var(--transition), border-color var(--transition), box-shadow var(--transition);
    }}
    .fig-card:hover {{
      transform: translateY(-2px);
      border-color: var(--primary);
      box-shadow: var(--shadow-md);
    }}
    .fig-img-wrap {{
      width: 100%;
      height: 220px;
      background: #121110;
      display: flex;
      align-items: center;
      justify-content: center;
      overflow: hidden;
      border-bottom: 1px solid var(--border);
    }}
    [data-theme="light"] .fig-img-wrap {{
      background: #f4efe6;
    }}
    .fig-img-wrap img {{
      max-width: 100%;
      max-height: 100%;
      object-fit: contain;
      transition: transform 0.2s ease;
    }}
    .fig-card:hover .fig-img-wrap img {{ transform: scale(1.02); }}

    .fig-card-body {{
      padding: 12px 14px;
      display: flex;
      flex-direction: column;
      gap: 7px;
      flex: 1;
    }}
    .fig-badge-row {{
      display: flex;
      align-items: center;
      justify-content: space-between;
    }}
    .fig-num-badge {{
      font-size: 11px;
      font-weight: 700;
      color: #f97316;
      background: rgba(249, 115, 22, 0.12);
      border: 1px solid rgba(249, 115, 22, 0.3);
      padding: 2px 7px;
      border-radius: 4px;
      font-family: "Geist Mono", monospace;
    }}
    [data-theme="light"] .fig-num-badge {{
      color: #c2410c;
      border-color: rgba(194, 65, 12, 0.3);
    }}
    .fig-page-info {{
      font-size: 11px;
      color: var(--text-faint);
    }}
    .fig-caption-text {{
      font-size: 12px;
      line-height: 1.45;
      color: var(--text-muted);
      display: -webkit-box;
      -webkit-line-clamp: 3;
      -webkit-box-orient: vertical;
      overflow: hidden;
    }}

    /* Tab 4: Methodology & Benchmarks */
    .benchmarks-pane-wrap {{
      width: 100%;
      height: 100%;
      overflow-y: auto;
      padding: 24px;
    }}
    .benchmarks-container {{
      max-width: 980px;
      margin: 0 auto;
      display: flex;
      flex-direction: column;
      gap: 20px;
    }}
    .kpi-cards-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 14px;
    }}
    .kpi-card {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: var(--radius-md);
      padding: 14px 16px;
      display: flex;
      flex-direction: column;
      gap: 6px;
      box-shadow: var(--shadow-sm);
    }}
    .kpi-label {{
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--text-faint);
      display: flex;
      align-items: center;
      gap: 6px;
    }}
    .kpi-val {{
      font-size: 14px;
      font-weight: 600;
      color: var(--text);
      line-height: 1.4;
    }}
    .kpi-sub {{
      font-size: 12px;
      color: var(--text-muted);
      line-height: 1.4;
    }}
    .report-box {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: var(--radius-md);
      padding: 22px;
      box-shadow: var(--shadow-sm);
    }}
    .report-box h2 {{
      font-size: 16px;
      font-weight: 700;
      margin-bottom: 12px;
      color: #ef4444;
    }}
    [data-theme="light"] .report-box h2 {{
      color: var(--primary);
    }}
    .report-box table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 13px;
      margin: 12px 0;
    }}
    .report-box th, .report-box td {{
      border: 1px solid var(--border);
      padding: 7px 11px;
      text-align: left;
    }}
    .report-box th {{
      background: var(--surface-elevated);
      color: var(--text);
      font-weight: 600;
    }}

    /* Lightbox Modal */
    .lightbox-modal {{
      position: fixed;
      inset: 0;
      background: rgba(14, 13, 12, 0.94);
      backdrop-filter: blur(8px);
      z-index: 200;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 24px;
    }}
    .lightbox-modal.active {{ display: flex; }}
    .lightbox-card {{
      background: var(--surface);
      border: 1px solid var(--border-strong);
      border-radius: var(--radius-lg);
      max-width: 1100px;
      max-height: 94vh;
      width: 100%;
      display: flex;
      flex-direction: column;
      overflow: hidden;
      box-shadow: var(--shadow-lg);
      position: relative;
    }}
    .lightbox-header {{
      padding: 12px 18px;
      border-bottom: 1px solid var(--border);
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
    }}
    .lightbox-header-title {{
      font-size: 13px;
      font-weight: 700;
      color: var(--text);
    }}
    .lightbox-img-area {{
      flex: 1;
      background: #0e0d0c;
      display: flex;
      align-items: center;
      justify-content: center;
      overflow: hidden;
      padding: 16px;
      position: relative;
      min-height: 380px;
    }}
    [data-theme="light"] .lightbox-img-area {{
      background: #f4efe6;
    }}
    .lightbox-img-area img {{
      max-width: 100%;
      max-height: 62vh;
      object-fit: contain;
    }}
    .lightbox-nav-btn {{
      position: absolute;
      top: 50%;
      transform: translateY(-50%);
      width: 38px;
      height: 38px;
      border-radius: 50%;
      background: rgba(26, 24, 22, 0.85);
      border: 1px solid var(--border-strong);
      color: var(--text);
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      transition: background var(--transition), transform var(--transition);
      z-index: 5;
    }}
    .lightbox-nav-btn:hover {{
      background: var(--surface-hover);
      color: #ef4444;
      transform: translateY(-50%) scale(1.08);
    }}
    [data-theme="light"] .lightbox-nav-btn:hover {{
      color: var(--primary);
    }}
    .lightbox-nav-prev {{ left: 16px; }}
    .lightbox-nav-next {{ right: 16px; }}
    .lightbox-caption-area {{
      padding: 14px 18px;
      border-top: 1px solid var(--border);
      font-size: 12.5px;
      color: var(--text-muted);
      line-height: 1.5;
      max-height: 120px;
      overflow-y: auto;
    }}

    /* Dropdown Popover Menu */
    .dropdown-menu {{
      position: absolute;
      top: 100%;
      right: 0;
      margin-top: 6px;
      background: var(--surface);
      border: 1px solid var(--border-strong);
      border-radius: var(--radius-md);
      box-shadow: var(--shadow-lg);
      padding: 6px;
      min-width: 190px;
      display: none;
      flex-direction: column;
      gap: 2px;
      z-index: 30;
    }}
    .dropdown-menu.active {{ display: flex; }}
    .dropdown-item {{
      display: flex;
      align-items: center;
      gap: 8px;
      padding: 7px 10px;
      font-size: 12px;
      color: var(--text);
      text-decoration: none;
      border-radius: var(--radius-sm);
      transition: background var(--transition);
    }}
    .dropdown-item:hover {{
      background: var(--surface-hover);
      color: #ef4444;
    }}
    [data-theme="light"] .dropdown-item:hover {{
      color: var(--primary);
    }}

    /* ==========================================================================
       RESPONSIVE & MOBILE VIEWPORT STABILITY FIXES (@media max-width: 768px)
       ========================================================================== */
    @media (max-width: 1240px) {{
      .research-grid {{ grid-template-columns: repeat(2, minmax(0, 1fr)); }}
    }}

    @media (max-width: 900px) {{
      .research-grid.list-view .research-card {{
        flex-direction: column;
        align-items: stretch;
      }}
      .research-grid.list-view .card-row-meta {{
        flex: none;
      }}
    }}

    @media (max-width: 768px) {{
      /* Root Cause C: Main Container & Padding */
      main.library-main {{
        padding: 12px 12px 30px 12px !important;
        gap: 14px !important;
        box-sizing: border-box !important;
      }}

      /* Top Header Mobile Compacting */
      header {{
        padding: 0 12px !important;
        height: 52px !important;
      }}
      .stats-pills {{
        display: none !important;
      }}
      .brand-title {{
        font-size: 14px !important;
      }}
      .brand-tag {{
        display: none !important;
      }}
      .btn-action span {{
        display: none !important;
      }}
      .btn-action {{
        padding: 6px 8px !important;
      }}

      /* Hub Navigation Tabs */
      .hub-main-tabs {{
        margin-bottom: 8px !important;
        padding-bottom: 8px !important;
        gap: 6px !important;
      }}
      .hub-tab-btn {{
        padding: 7px 12px !important;
        font-size: 12.5px !important;
      }}

      /* Root Cause C: Toolbar & Search Input without 320px blowout */
      .library-toolbar {{
        padding: 10px 12px !important;
        gap: 10px !important;
        border-radius: var(--radius-lg) !important;
      }}
      .toolbar-row {{
        flex-direction: column !important;
        align-items: stretch !important;
        gap: 8px !important;
      }}
      .search-input-wrap {{
        min-width: 0 !important;
        width: 100% !important;
      }}
      .view-switcher {{
        align-self: flex-start !important;
      }}

      /* Root Cause B: Filter Chip Row as Single Horizontal Swipeable Track */
      .filter-chips-row {{
        flex-wrap: nowrap !important;
        overflow-x: auto !important;
        -webkit-overflow-scrolling: touch !important;
        padding-bottom: 4px !important;
        scrollbar-width: none !important;
        width: 100% !important;
        gap: 6px !important;
      }}
      .filter-chips-row::-webkit-scrollbar {{
        display: none !important;
      }}
      .filter-chip {{
        flex-shrink: 0 !important;
        white-space: nowrap !important;
        padding: 5px 11px !important;
        font-size: 11.5px !important;
      }}

      /* Root Cause E: 1-Column Layout for Cards Grid */
      .research-grid {{
        grid-template-columns: 1fr !important;
        gap: 14px !important;
      }}
      .research-card {{
        padding: 16px 16px !important;
      }}
      .card-title {{
        font-size: 14.5px !important;
      }}

      /* Extended Table Mobile Adaptability */
      .extended-container {{
        padding: 12px !important;
      }}
      .extended-header-row {{
        flex-direction: column !important;
        align-items: stretch !important;
      }}

      /* Root Cause A: Full-Screen Mobile Sheet for Modal Reader */
      .reader-modal-overlay {{
        padding: 0 !important;
        inset: 0 !important;
        position: fixed !important;
        width: 100vw !important;
        height: 100dvh !important;
        max-width: 100vw !important;
        max-height: 100dvh !important;
      }}
      .reader-modal-box {{
        width: 100vw !important;
        height: 100dvh !important;
        max-width: 100vw !important;
        max-height: 100dvh !important;
        inset: 0 !important;
        border-radius: 0 !important;
        padding: 0 !important;
        position: fixed !important;
        margin: 0 !important;
        border: none !important;
        box-shadow: none !important;
      }}

      /* Sticky Modal Header */
      .modal-header {{
        position: sticky !important;
        top: 0 !important;
        z-index: 50 !important;
        padding: 10px 12px !important;
        gap: 8px !important;
      }}
      .modal-header-top {{
        display: flex !important;
        flex-direction: column !important;
        align-items: stretch !important;
        gap: 8px !important;
      }}
      .modal-title-col {{
        width: 100% !important;
      }}
      .modal-paper-title {{
        font-size: 14px !important;
        line-height: 1.35 !important;
        word-break: break-word !important;
      }}
      .modal-actions-group {{
        display: flex !important;
        align-items: center !important;
        justify-content: space-between !important;
        width: 100% !important;
        gap: 6px !important;
        flex-wrap: wrap !important;
      }}

      /* Minimum 44px Tap Target for Close Button */
      .btn-close-modal {{
        min-width: 44px !important;
        min-height: 44px !important;
        width: 44px !important;
        height: 44px !important;
        touch-action: manipulation !important;
        margin-left: auto !important;
      }}

      /* Modal Tabs Horizontal Swipe */
      .modal-nav-row {{
        flex-direction: column !important;
        align-items: stretch !important;
        gap: 6px !important;
      }}
      .modal-view-tabs {{
        flex-wrap: nowrap !important;
        overflow-x: auto !important;
        -webkit-overflow-scrolling: touch !important;
        scrollbar-width: none !important;
        width: 100% !important;
        padding: 2px !important;
      }}
      .modal-view-tabs::-webkit-scrollbar {{
        display: none !important;
      }}
      .modal-tab-btn {{
        flex-shrink: 0 !important;
        white-space: nowrap !important;
        padding: 6px 10px !important;
        font-size: 11.5px !important;
      }}
      .modal-utility-group {{
        display: flex !important;
        justify-content: flex-end !important;
        width: 100% !important;
      }}

      /* Root Cause D: Hide 270px TOC Sidebar on Mobile */
      .tree-toc-sidebar {{
        display: none !important;
      }}
      .tree-article-wrap {{
        width: 100% !important;
        max-width: 100% !important;
        padding: 14px 12px 60px 12px !important;
      }}

      /* Root Cause E: 1 Column for Gallery and Benchmarks */
      .gallery-pane-wrap,
      .benchmarks-pane-wrap {{
        padding: 12px !important;
      }}
      .gallery-grid {{
        grid-template-columns: 1fr !important;
        gap: 12px !important;
      }}
      .kpi-cards-grid {{
        grid-template-columns: 1fr !important;
        gap: 10px !important;
      }}

      /* Root Cause F: Markmap Touch Trapping Protection */
      .mindmap-touch-bar {{
        display: flex !important;
      }}
      .mindmap-frame {{
        pointer-events: none; /* Prevents scroll interception by default on touch */
      }}
      .mindmap-frame.interactive {{
        pointer-events: auto; /* Active when explicitly toggled */
      }}
    }}
  </style>
</head>
<body>

  <!-- Top Sticky Navigation Header -->
  <header>
    <div class="brand-wrap">
      <div class="brand-logo-badge">
        <svg class="icon icon-md" viewBox="0 0 24 24">
          <path d="M4 19.5v-15A2.5 2.5 0 0 1 6.5 2H20v20H6.5a2.5 2.5 0 0 1-2.5-2.5Z"/>
          <path d="M6 6h10"/><path d="M6 10h10"/><path d="M6 14h6"/>
        </svg>
      </div>
      <div class="brand-title-wrap">
        <span class="brand-title">AutoML & MBR Research Hub</span>
        <span class="brand-tag">Kỹ Thuật Màng Lọc & Xử Lý Nước</span>
      </div>
    </div>

    <!-- Quantitative Corpus Overview Pills -->
    <div class="stats-pills">
      <div class="stat-pill"><strong>30</strong> Chọn Lọc</div>
      <div class="stat-pill"><strong>65</strong> Tham Khảo</div>
      <div class="stat-pill"><strong>95</strong> Tổng Số Bài</div>
      <div class="stat-pill"><strong>2018–2026</strong></div>
    </div>

    <!-- Theme & Repo Actions -->
    <div class="nav-actions">
      <button class="btn-action" id="themeToggleBtn" title="Chuyển chế độ Sáng / Tối">
        <svg class="icon icon-sm" id="themeToggleIcon" viewBox="0 0 24 24">
          <circle cx="12" cy="12" r="5"/><line x1="12" y1="1" x2="12" y2="3"/><line x1="12" y1="21" x2="12" y2="23"/>
          <line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/>
          <line x1="1" y1="12" x2="3" y2="12"/><line x1="21" y1="12" x2="23" y2="12"/>
          <line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/>
        </svg>
        <span>Giao Diện</span>
      </button>
      <a class="btn-action" href="https://github.com/nguyendoanhcmut/paper-tab-automl" target="_blank" title="Xem Kho Lưu Trữ GitHub">
        <svg class="icon icon-sm" viewBox="0 0 24 24">
          <path d="M15 22v-4a4.8 4.8 0 0 0-1-3.5c3 0 6-2 6-5.5.08-1.25-.27-2.48-1-3.5.28-1.15.28-2.35 0-3.5 0 0-1 0-3 1.5-2.64-.5-5.36-.5-8 0C6 2 5 2 5 2c-.3 1.15-.3 2.35 0 3.5A5.403 5.403 0 0 0 4 9c0 3.5 3 5.5 6 5.5-.39.49-.68 1.05-.85 1.65-.17.6-.22 1.23-.15 1.85v4"/>
          <path d="M9 18c-4.51 2-5-2-7-2"/>
        </svg>
        <span>GitHub</span>
      </a>
    </div>
  </header>

  <!-- Main Showcase Area -->
  <main class="library-main">

    <!-- Top Master Tabs Navigation: Tab 1 vs Tab 2 -->
    <nav class="hub-main-tabs" id="hubMainTabs">
      <button class="hub-tab-btn active" id="tabCoreBtn" data-target="core">
        <svg class="icon icon-sm" viewBox="0 0 24 24">
          <path d="M4 19.5v-15A2.5 2.5 0 0 1 6.5 2H20v20H6.5a2.5 2.5 0 0 1-2.5-2.5Z"/>
          <path d="M6 6h10"/><path d="M6 10h10"/>
        </svg>
        <span>30 bài chọn lọc</span>
      </button>
      <button class="hub-tab-btn" id="tabExtendedBtn" data-target="extended">
        <svg class="icon icon-sm" viewBox="0 0 24 24">
          <path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"/>
        </svg>
        <span>Tài liệu tham khảo (65 bài)</span>
      </button>
    </nav>

    <!-- ==================== PANE 1: CORE PAPERS (30 BÀI) ==================== -->
    <section class="hub-pane active" id="paneCore">
      
      <!-- Control Toolbar (Search, Filter Chips, View Toggle) -->
      <section class="library-toolbar">
        <div class="toolbar-row">
          <!-- Live Search Input -->
          <div class="search-input-wrap">
            <svg class="icon icon-sm search-icon-pos" viewBox="0 0 24 24">
              <circle cx="11" cy="11" r="8"/><line x1="21" x2="16.65" y1="21" y2="16.65"/>
            </svg>
            <input type="text" id="searchInput" placeholder="Tìm theo mã bài [M018], thuật toán (SHAP, FLAML, ANN), tác giả, thông số TMP, HRT...">
            <button class="search-clear-btn" id="searchClearBtn" title="Xóa tìm kiếm">
              <svg class="icon icon-xs" viewBox="0 0 24 24"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
            </button>
          </div>

          <!-- View Switcher (Grid / List) -->
          <div class="view-switcher">
            <button class="btn-view-toggle active" id="viewGridBtn" title="Chế độ xem Lưới Thẻ">
              <svg class="icon icon-xs" viewBox="0 0 24 24">
                <rect width="7" height="7" x="3" y="3" rx="1"/><rect width="7" height="7" x="14" y="3" rx="1"/>
                <rect width="7" height="7" x="14" y="14" rx="1"/><rect width="7" height="7" x="3" y="14" rx="1"/>
              </svg>
              <span>Lưới</span>
            </button>
            <button class="btn-view-toggle" id="viewListBtn" title="Chế độ xem Danh Sách">
              <svg class="icon icon-xs" viewBox="0 0 24 24">
                <line x1="8" x2="21" y1="6" y2="6"/><line x1="8" x2="21" y1="12" y2="12"/><line x1="8" x2="21" y1="18" y2="18"/>
                <line x1="3" x2="3.01" y1="6" y2="6"/><line x1="3" x2="3.01" y1="12" y2="12"/><line x1="3" x2="3.01" y1="18" y2="18"/>
              </svg>
              <span>Danh Sách</span>
            </button>
          </div>
        </div>

        <!-- Filter Chips Row (Swipeable Track on Mobile) -->
        <div class="filter-chips-row" id="filterChipsRow">
          <button class="filter-chip active" data-filter="all">
            <span>Tất Cả</span>
            <span class="filter-chip-count" id="chipCountAll">30</span>
          </button>
          <button class="filter-chip" data-filter="mbr">
            <span>MBR & Màng Lọc</span>
            <span class="filter-chip-count" id="chipCountMbr">16</span>
          </button>
          <button class="filter-chip" data-filter="automl">
            <span>AutoML & XAI</span>
            <span class="filter-chip-count" id="chipCountAutoml">14</span>
          </button>
          <button class="filter-chip" data-filter="anammox">
            <span>Anammox</span>
            <span class="filter-chip-count">1</span>
          </button>
          <button class="filter-chip" data-filter="transfer">
            <span>Transfer Learning</span>
            <span class="filter-chip-count">1</span>
          </button>
          <button class="filter-chip" data-filter="review">
            <span>Tổng Quan / Review</span>
            <span class="filter-chip-count">2</span>
          </button>
          <button class="filter-chip" data-filter="water_quality">
            <span>Chất Lượng Nước</span>
            <span class="filter-chip-count">2</span>
          </button>
        </div>
      </section>

      <!-- Results Status Info -->
      <div class="results-count-bar">
        <div>Hiển thị <strong id="visibleCountText" style="color: var(--text);">30</strong> bài nghiên cứu chọn lọc</div>
        <div id="filterStatusText">Tài liệu y văn 2018–2026</div>
      </div>

      <!-- Research Cards Grid -->
      <div class="research-grid" id="researchGrid"></div>
    </section>

    <!-- ==================== PANE 2: EXTENDED CATALOG (65 BÀI) ==================== -->
    <section class="hub-pane" id="paneExtended">
      <div class="extended-container">
        <div class="extended-header-row">
          <div class="extended-info-badge">
            <svg class="icon icon-sm" viewBox="0 0 24 24" style="color: var(--accent-bio);"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10"/><path d="m9 12 2 2 4-4"/></svg>
            <span>Tài liệu tham khảo: <strong id="extCountText">65</strong> bài báo có bản dịch song ngữ (-dual.pdf)</span>
          </div>

          <!-- Quick Filter for Extended Catalog -->
          <div class="search-input-wrap" style="max-width: 380px;">
            <svg class="icon icon-sm search-icon-pos" viewBox="0 0 24 24">
              <circle cx="11" cy="11" r="8"/><line x1="21" x2="16.65" y1="21" y2="16.65"/>
            </svg>
            <input type="text" id="extSearchInput" placeholder="Lọc nhanh theo mã bài [B008], tên bài, tác giả, năm...">
          </div>
        </div>

        <div class="extended-table-wrap">
          <table class="extended-table">
            <thead>
              <tr>
                <th style="width: 100px;">Mã Bài (PID)</th>
                <th class="ext-title-col">Tên Bài Báo (Việt / Anh)</th>
                <th style="width: 220px;">Tác Giả & Tạp Chí</th>
                <th style="width: 80px; text-align: center;">Năm</th>
                <th style="width: 160px; text-align: right;">Bản Dịch Song Ngữ</th>
              </tr>
            </thead>
            <tbody id="extendedTableBody"></tbody>
          </table>
        </div>
      </div>
    </section>

  </main>

  <!-- Detail Modal Reader (Full 4-Tab Interactive Suite) -->
  <div class="reader-modal-overlay" id="readerModalOverlay">
    <div class="reader-modal-box">
      
      <!-- Modal Header -->
      <div class="modal-header">
        <div class="modal-header-top">
          <div class="modal-title-col">
            <div class="modal-meta-row">
              <span class="pid-badge" id="modalPidBadge">[M001]</span>
              <span class="paper-num-badge" id="modalPaperNumBadge">#01</span>
              <span class="category-tag theme-emerald" id="modalCategoryTag">AutoML & MBR</span>
              <span id="modalMetaYearJournal" style="font-family: 'Geist Mono', monospace; font-size: 11.5px;">2026 • Elsevier</span>
              <span id="modalLineageTag" style="display: inline-flex; align-items: center; gap: 4px; color: var(--accent-bio); font-weight: 600;">
                <svg class="icon icon-xs" viewBox="0 0 24 24"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10"/><path d="m9 12 2 2 4-4"/></svg>
                <span>Đã Xác Thực Lineage</span>
              </span>
            </div>
            <h1 class="modal-paper-title" id="modalPaperTitle">Tiêu đề bài báo nghiên cứu</h1>
            <div class="modal-paper-subtitle" id="modalPaperSubtitle">Điểm nhấn giải pháp kỹ thuật</div>
            <div class="card-source" id="modalPaperAuthors" style="margin-bottom: 0;">
              <svg class="icon icon-xs" viewBox="0 0 24 24"><path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
              <span>Tác giả & Tạp chí</span>
            </div>
          </div>

          <!-- Quick Action Buttons -->
          <div class="modal-actions-group">
            <a class="btn-pdf" id="modalPdfOrigBtn" href="#" target="_blank" title="Mở tệp PDF gốc tiếng Anh">
              <svg class="icon icon-sm" viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg>
              <span>PDF Gốc (EN)</span>
            </a>
            <a class="btn-pdf bilingual" id="modalPdfBilingualBtn" href="#" target="_blank" title="Mở tệp PDF song ngữ Việt - Anh">
              <svg class="icon icon-sm" viewBox="0 0 24 24"><path d="m5 8 6 6"/><path d="m4 14 6-6 2-3"/><path d="M2 5h12"/><path d="M7 2h1"/><path d="m22 22-5-10-5 10"/><path d="M14 18h6"/></svg>
              <span>Song Ngữ (VI-EN)</span>
            </a>
            <button class="btn-close-modal" id="modalCloseBtn" title="Đóng cửa sổ đọc (Esc)">
              <svg class="icon icon-sm" viewBox="0 0 24 24"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
            </button>
          </div>
        </div>

        <!-- Modal View Tabs Bar -->
        <div class="modal-nav-row">
          <div class="modal-view-tabs" id="modalViewTabs">
            <button class="modal-tab-btn active" data-tab="mindmap">
              <svg class="icon icon-sm" viewBox="0 0 24 24"><circle cx="18" cy="5" r="3"/><circle cx="6" cy="12" r="3"/><circle cx="18" cy="19" r="3"/><line x1="8.59" x2="15.42" y1="13.51" y2="17.49"/><line x1="15.41" x2="8.59" y1="6.51" y2="10.49"/></svg>
              <span>Mind Map (Markmap)</span>
            </button>
            <button class="modal-tab-btn" data-tab="tree">
              <svg class="icon icon-sm" viewBox="0 0 24 24"><line x1="21" x2="3" y1="6" y2="6"/><line x1="15" x2="3" y1="12" y2="12"/><line x1="17" x2="3" y1="18" y2="18"/></svg>
              <span>Knowledge Tree (Markdown + KaTeX)</span>
            </button>
            <button class="modal-tab-btn" data-tab="gallery">
              <svg class="icon icon-sm" viewBox="0 0 24 24"><rect width="18" height="18" x="3" y="3" rx="2" ry="2"/><circle cx="8.5" cy="8.5" r="1.5"/><polyline points="21 15 16 10 5 21"/></svg>
              <span>Đồ Hình & Bảng Biểu (<span id="modalFigCountBadge">0</span>)</span>
            </button>
            <button class="modal-tab-btn" data-tab="benchmarks">
              <svg class="icon icon-sm" viewBox="0 0 24 24"><line x1="18" x2="18" y1="20" y2="10"/><line x1="12" x2="12" y1="20" y2="4"/><line x1="6" x2="6" y1="20" y2="14"/></svg>
              <span>Thông Số & Benchmarks</span>
            </button>
          </div>

          <div class="modal-utility-group">
            <a class="btn-action" id="modalStandaloneBtn" target="_blank" href="#" title="Mở nội dung trong tab trình duyệt độc lập">
              <svg class="icon icon-xs" viewBox="0 0 24 24"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" x2="21" y1="14" y2="3"/></svg>
              <span>Tab Mới</span>
            </a>
            <button class="btn-action" id="modalFullscreenBtn" title="Chuyển đổi toàn màn hình">
              <svg class="icon icon-xs" viewBox="0 0 24 24"><path d="M8 3H5a2 2 0 0 0-2 2v3"/><path d="M21 8V5a2 2 0 0 0-2-2h-3"/><path d="M3 16v3a2 2 0 0 0 2 2h3"/><path d="M16 21h3a2 2 0 0 0 2-2v-3"/></svg>
            </button>
          </div>
        </div>
      </div>

      <!-- Modal Body (Panes) -->
      <div class="modal-body">
        <!-- Pane 1: Mindmap with Touch Trapping Protection -->
        <div class="modal-pane active" id="paneMindmap">
          <div class="mindmap-touch-bar" id="mindmapTouchBar">
            <span>Chạm nút để kích hoạt kéo Mindmap • Vuốt ngoài để cuộn</span>
            <button class="btn-touch-toggle" id="btnTouchToggle">Bật tương tác chạm</button>
          </div>
          <iframe class="mindmap-frame" id="mindmapIframe" src=""></iframe>
          <div id="mindmapPlaceholder" style="display: none; padding: 40px; text-align: center;"></div>
        </div>

        <!-- Pane 2: Knowledge Tree Markdown -->
        <div class="modal-pane" id="paneTree">
          <div class="tree-layout">
            <div class="tree-article-wrap" id="treeArticleWrap">
              <div class="tree-article-inner" id="treeArticleInner">Đang tải cây tri thức markdown...</div>
            </div>
            <aside class="tree-toc-sidebar" id="treeTocSidebar">
              <div class="tree-toc-title">
                <svg class="icon icon-xs" viewBox="0 0 24 24"><line x1="21" x2="3" y1="6" y2="6"/><line x1="15" x2="3" y1="12" y2="12"/><line x1="17" x2="3" y1="18" y2="18"/></svg>
                <span>Mục Lục Cây Tri Thức</span>
              </div>
              <div id="treeTocList"></div>
            </aside>
          </div>
        </div>

        <!-- Pane 3: Figures Gallery -->
        <div class="modal-pane" id="paneGallery">
          <div class="gallery-pane-wrap">
            <div class="gallery-grid" id="galleryGrid"></div>
          </div>
        </div>

        <!-- Pane 4: Benchmarks & Methodology -->
        <div class="modal-pane" id="paneBenchmarks">
          <div class="benchmarks-pane-wrap">
            <div class="benchmarks-container" id="benchmarksContainer"></div>
          </div>
        </div>
      </div>

    </div>
  </div>

  <!-- High-Res Lightbox Modal -->
  <div class="lightbox-modal" id="lightboxModal">
    <div class="lightbox-card">
      <div class="lightbox-header">
        <div class="lightbox-header-title" id="lightboxTitle">Xem Đồ Hình Độ Phân Giải Cao</div>
        <button class="btn-action" id="lightboxCloseBtn">
          <svg class="icon icon-sm" viewBox="0 0 24 24"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
          <span>Đóng (Esc)</span>
        </button>
      </div>
      <div class="lightbox-img-area">
        <button class="lightbox-nav-btn lightbox-nav-prev" id="lightboxPrevBtn" title="Đồ hình trước (Mũi tên trái)">
          <svg class="icon icon-md" viewBox="0 0 24 24"><path d="m15 18-6-6 6-6"/></svg>
        </button>
        <img id="lightboxImg" src="" alt="Đồ hình khoa học">
        <button class="lightbox-nav-btn lightbox-nav-next" id="lightboxNextBtn" title="Đồ hình tiếp theo (Mũi tên phải)">
          <svg class="icon icon-md" viewBox="0 0 24 24"><path d="m9 18 6-6-6-6"/></svg>
        </button>
      </div>
      <div class="lightbox-caption-area" id="lightboxCaption"></div>
    </div>
  </div>

  <!-- Client-Side Architecture -->
  <script>
    const papersCatalog = {catalog_json_str};
    const extendedCatalog = {extended_json_str};

    const basePath = 'branche_v2/';

    // State Variables
    let currentFilter = 'all';
    let searchQuery = '';
    let extSearchQuery = '';
    let currentViewMode = 'grid'; // 'grid' | 'list'
    let activePaper = papersCatalog[0] || null;
    let activeModalTab = 'mindmap';
    let currentLightboxIdx = 0;
    let activeMasterTab = 'core'; // 'core' | 'extended'

    // DOM Elements Cache
    const hubMainTabs = document.getElementById('hubMainTabs');
    const paneCore = document.getElementById('paneCore');
    const paneExtended = document.getElementById('paneExtended');

    const searchInput = document.getElementById('searchInput');
    const searchClearBtn = document.getElementById('searchClearBtn');
    const filterChipsRow = document.getElementById('filterChipsRow');
    const visibleCountText = document.getElementById('visibleCountText');
    const filterStatusText = document.getElementById('filterStatusText');
    const researchGrid = document.getElementById('researchGrid');
    const viewGridBtn = document.getElementById('viewGridBtn');
    const viewListBtn = document.getElementById('viewListBtn');

    // Extended Catalog Elements
    const extSearchInput = document.getElementById('extSearchInput');
    const extendedTableBody = document.getElementById('extendedTableBody');
    const extCountText = document.getElementById('extCountText');

    // Modal Elements
    const readerModalOverlay = document.getElementById('readerModalOverlay');
    const modalCloseBtn = document.getElementById('modalCloseBtn');
    const modalPidBadge = document.getElementById('modalPidBadge');
    const modalPaperNumBadge = document.getElementById('modalPaperNumBadge');
    const modalCategoryTag = document.getElementById('modalCategoryTag');
    const modalMetaYearJournal = document.getElementById('modalMetaYearJournal');
    const modalPaperTitle = document.getElementById('modalPaperTitle');
    const modalPaperSubtitle = document.getElementById('modalPaperSubtitle');
    const modalPaperAuthors = document.getElementById('modalPaperAuthors');
    const modalPdfOrigBtn = document.getElementById('modalPdfOrigBtn');
    const modalPdfBilingualBtn = document.getElementById('modalPdfBilingualBtn');
    const modalViewTabs = document.getElementById('modalViewTabs');
    const modalFigCountBadge = document.getElementById('modalFigCountBadge');
    const modalStandaloneBtn = document.getElementById('modalStandaloneBtn');
    const modalFullscreenBtn = document.getElementById('modalFullscreenBtn');
    const modalLineageTag = document.getElementById('modalLineageTag');

    const mindmapIframe = document.getElementById('mindmapIframe');
    const mindmapPlaceholder = document.getElementById('mindmapPlaceholder');
    const btnTouchToggle = document.getElementById('btnTouchToggle');

    const treeArticleInner = document.getElementById('treeArticleInner');
    const treeTocList = document.getElementById('treeTocList');
    const galleryGrid = document.getElementById('galleryGrid');
    const benchmarksContainer = document.getElementById('benchmarksContainer');

    // Lightbox Elements
    const lightboxModal = document.getElementById('lightboxModal');
    const lightboxImg = document.getElementById('lightboxImg');
    const lightboxTitle = document.getElementById('lightboxTitle');
    const lightboxCaption = document.getElementById('lightboxCaption');
    const lightboxCloseBtn = document.getElementById('lightboxCloseBtn');
    const lightboxPrevBtn = document.getElementById('lightboxPrevBtn');
    const lightboxNextBtn = document.getElementById('lightboxNextBtn');

    // Theme Elements
    const themeToggleBtn = document.getElementById('themeToggleBtn');
    const themeToggleIcon = document.getElementById('themeToggleIcon');

    // Master Hub Tabs Handling
    hubMainTabs.addEventListener('click', (e) => {{
      const btn = e.target.closest('.hub-tab-btn');
      if (!btn) return;
      document.querySelectorAll('.hub-tab-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      activeMasterTab = btn.dataset.target;

      if (activeMasterTab === 'core') {{
        paneCore.classList.add('active');
        paneExtended.classList.remove('active');
        renderLibrary();
      }} else {{
        paneCore.classList.remove('active');
        paneExtended.classList.add('active');
        renderExtendedTable();
      }}
    }});

    // Render Tab 1 (Core 30 Papers)
    function renderLibrary() {{
      const query = searchQuery.toLowerCase();

      const filtered = papersCatalog.filter(p => {{
        // Category filter
        if (currentFilter !== 'all') {{
          const matchTag = (p.filter_tags || []).includes(currentFilter);
          const matchKey = p.category_key === currentFilter;
          if (!matchTag && !matchKey) return false;
        }}

        // Search query
        if (query) {{
          const inTitleVn = (p.title_vn || '').toLowerCase().includes(query);
          const inTitleEn = (p.title_en || p.title || '').toLowerCase().includes(query);
          const inPid = (p.pid || '').toLowerCase().includes(query);
          const inAuthors = (p.authors_short || p.authors_full || '').toLowerCase().includes(query);
          const inTags = (p.filter_tags || []).some(t => t.toLowerCase().includes(query));
          const inSummary = JSON.stringify(p.summary || {{}}).toLowerCase().includes(query);
          if (!inTitleVn && !inTitleEn && !inPid && !inAuthors && !inTags && !inSummary) return false;
        }}
        return true;
      }});

      visibleCountText.textContent = filtered.length;
      researchGrid.innerHTML = '';

      if (filtered.length === 0) {{
        researchGrid.innerHTML = `
          <div style="grid-column: 1 / -1; padding: 60px 20px; text-align: center; color: var(--text-muted);">
            <svg class="icon icon-lg" viewBox="0 0 24 24" style="margin-bottom: 12px; stroke-width: 1.5; color: var(--text-faint);">
              <circle cx="11" cy="11" r="8"/><line x1="21" x2="16.65" y1="21" y2="16.65"/>
            </svg>
            <h3 style="font-size: 15px; color: var(--text); margin-bottom: 6px;">Không tìm thấy công trình nghiên cứu phù hợp</h3>
            <p style="font-size: 13px;">Thử đổi từ khóa hoặc xóa bộ lọc để hiển thị danh sách đầy đủ 30 bài.</p>
          </div>
        `;
        return;
      }}

      filtered.forEach(p => {{
        const card = document.createElement('article');
        card.className = 'research-card';
        card.setAttribute('data-id', p.id);

        const themeClass = `theme-${{p.category_theme || 'emerald'}}`;
        const nodesFmt = (p.nodes || 0).toLocaleString('vi-VN');
        const figsCount = p.figures || (p.figures_list ? p.figures_list.length : 0);
        const pagesCount = p.pages || 0;
        const pidDisplay = p.pid ? `[${{p.pid}}]` : `[#${{String(p.id).padStart(2, '0')}}]`;

        card.innerHTML = `
          <div class="card-row-meta">
            <div class="card-meta-left">
              <span class="pid-badge">${{pidDisplay}}</span>
              <span class="paper-num-badge">#${{String(p.id).padStart(2, '0')}}</span>
              <span class="category-tag ${{themeClass}}">${{p.category || 'MBR'}}</span>
            </div>
            <span class="card-id-slug">${{p.year}} • ${{p.journal_short || 'Research'}}</span>
          </div>
          
          <h2 class="card-title" title="${{p.title_en || p.title}}">${{p.title_vn || p.title}}</h2>
          
          <div class="card-subtitle">${{p.subtitle_vn || (p.filter_tags || []).join(' • ')}}</div>
          
          <div class="card-source" title="${{p.authors_full || ''}} • ${{p.journal_full || ''}}">
            <svg class="icon icon-xs" viewBox="0 0 24 24"><path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
            <span>${{p.authors_short || 'Research Team'}} • ${{p.journal_full || ''}}</span>
          </div>
          
          <p class="card-desc">${{p.description_vn || p.summary?.domain || ''}}</p>
          
          <div class="sunken-metrics">
            <strong>${{figsCount}}</strong> đồ hình
            <span class="sunken-dot">•</span>
            <strong>${{nodesFmt}}</strong> nút tri thức
            <span class="sunken-dot">•</span>
            <strong>${{pagesCount}}</strong> trang
          </div>
          
          <div class="card-actions">
            <button class="btn-primary-card" data-action="explore">
              <svg class="icon icon-xs" viewBox="0 0 24 24" style="fill: currentColor; stroke: none;"><polygon points="5 3 19 12 5 21 5 3"/></svg>
              <span>Xem Cây Tri Thức</span>
            </button>
            <div style="display: flex; align-items: center; gap: 6px;">
              ${{p.pdf_bilingual ? `
                <a class="btn-pdf-badge" href="${{encodeURI(p.pdf_bilingual)}}" target="_blank" title="Mở trực tiếp bản dịch song ngữ PDF">
                  <svg class="icon icon-xs" viewBox="0 0 24 24"><path d="m5 8 6 6"/><path d="m4 14 6-6 2-3"/><path d="M2 5h12"/><path d="M7 2h1"/><path d="m22 22-5-10-5 10"/><path d="M14 18h6"/></svg>
                  <span>Song Ngữ</span>
                </a>
              ` : ''}}
              <div style="position: relative;">
                <button class="btn-secondary-card" data-action="toggle-menu" title="Tùy chọn mở tệp">
                  <svg class="icon icon-xs" viewBox="0 0 24 24"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" x2="21" y1="14" y2="3"/></svg>
                </button>
                <div class="dropdown-menu">
                  ${{p.html_file ? `
                    <a class="dropdown-item" href="${{basePath}}${{p.html_file}}" target="_blank">
                      <svg class="icon icon-xs" viewBox="0 0 24 24"><circle cx="18" cy="5" r="3"/><circle cx="6" cy="12" r="3"/><circle cx="18" cy="19" r="3"/><line x1="8.59" x2="15.42" y1="13.51" y2="17.49"/><line x1="15.41" x2="8.59" y1="6.51" y2="10.49"/></svg>
                      <span>Mở Mindmap Tab Mới</span>
                    </a>
                  ` : ''}}
                  ${{p.md_file ? `
                    <a class="dropdown-item" href="${{basePath}}${{p.md_file}}" target="_blank">
                      <svg class="icon icon-xs" viewBox="0 0 24 24"><line x1="21" x2="3" y1="6" y2="6"/><line x1="15" x2="3" y1="12" y2="12"/><line x1="17" x2="3" y1="18" y2="18"/></svg>
                      <span>Cây Tri Thức Markdown</span>
                    </a>
                  ` : ''}}
                  ${{p.pdf_original ? `<a class="dropdown-item" href="${{encodeURI(p.pdf_original)}}" target="_blank"><svg class="icon icon-xs" viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg><span>PDF Gốc (Tiếng Anh)</span></a>` : ''}}
                  ${{p.pdf_bilingual ? `<a class="dropdown-item" href="${{encodeURI(p.pdf_bilingual)}}" target="_blank"><svg class="icon icon-xs" viewBox="0 0 24 24"><path d="m5 8 6 6"/><path d="m4 14 6-6 2-3"/><path d="M2 5h12"/><path d="M7 2h1"/><path d="m22 22-5-10-5 10"/><path d="M14 18h6"/></svg><span>PDF Song Ngữ (VI-EN)</span></a>` : ''}}
                </div>
              </div>
            </div>
          </div>
        `;

        // Card Click Handler
        card.addEventListener('click', (e) => {{
          const menuBtn = e.target.closest('[data-action="toggle-menu"]');
          if (menuBtn) {{
            e.stopPropagation();
            const menu = card.querySelector('.dropdown-menu');
            document.querySelectorAll('.dropdown-menu').forEach(m => {{ if (m !== menu) m.classList.remove('active'); }});
            menu.classList.toggle('active');
            return;
          }}
          if (e.target.closest('.dropdown-menu') || e.target.closest('.btn-pdf-badge')) return;
          openReaderModal(p, 'mindmap');
        }});

        researchGrid.appendChild(card);
      }});
    }}

    // Render Tab 2: Extended 65 Papers Table
    function renderExtendedTable() {{
      const query = extSearchQuery.toLowerCase();

      const filtered = extendedCatalog.filter(p => {{
        if (!query) return true;
        const inPid = (p.pid || '').toLowerCase().includes(query);
        const inTitleVn = (p.title_vn || '').toLowerCase().includes(query);
        const inTitleEn = (p.title_en || '').toLowerCase().includes(query);
        const inAuthors = (p.authors || '').toLowerCase().includes(query);
        const inYear = String(p.year || '').includes(query);
        const inVenue = (p.venue || '').toLowerCase().includes(query);
        return inPid || inTitleVn || inTitleEn || inAuthors || inYear || inVenue;
      }});

      extCountText.textContent = filtered.length;
      extendedTableBody.innerHTML = '';

      if (filtered.length === 0) {{
        extendedTableBody.innerHTML = `
          <tr>
            <td colspan="5" style="text-align: center; padding: 40px; color: var(--text-muted);">
              Không tìm thấy tài liệu mở rộng nào khớp với "${{htmlEscape(extSearchQuery)}}"
            </td>
          </tr>
        `;
        return;
      }}

      filtered.forEach(p => {{
        const tr = document.createElement('tr');
        tr.innerHTML = `
          <td>
            <span class="pid-badge" style="font-size: 11.5px;">[${{p.pid}}]</span>
          </td>
          <td class="ext-title-col">
            <div class="ext-title-vn">${{p.title_vn}}</div>
            <div class="ext-title-en">${{p.title_en}}</div>
          </td>
          <td>
            <div style="font-weight: 500; color: var(--text);">${{p.authors}}</div>
            <div class="ext-meta-sub">${{p.venue}}</div>
          </td>
          <td style="text-align: center; font-family: 'Geist Mono', monospace; font-size: 12px; font-weight: 600;">
            ${{p.year}}
          </td>
          <td style="text-align: right;">
            <a class="btn-pdf bilingual" href="${{encodeURI(p.pdf_dual)}}" target="_blank" style="padding: 5px 11px; font-size: 11.5px;">
              <svg class="icon icon-xs" viewBox="0 0 24 24"><path d="m5 8 6 6"/><path d="m4 14 6-6 2-3"/><path d="M2 5h12"/><path d="M7 2h1"/><path d="m22 22-5-10-5 10"/><path d="M14 18h6"/></svg>
              <span>Song Ngữ (PDF)</span>
            </a>
          </td>
        `;
        extendedTableBody.appendChild(tr);
      }});
    }}

    // Helper: HTML Escape
    function htmlEscape(str) {{
      return String(str).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
    }}

    // Close dropdowns on outside click
    document.addEventListener('click', (e) => {{
      if (!e.target.closest('[data-action="toggle-menu"]')) {{
        document.querySelectorAll('.dropdown-menu').forEach(m => m.classList.remove('active'));
      }}
    }});

    // Open Detail Modal Reader
    function openReaderModal(paper, defaultTab = 'mindmap') {{
      activePaper = paper;
      document.body.style.overflow = 'hidden';

      // Update Modal Header Information
      modalPidBadge.textContent = paper.pid ? `[${{paper.pid}}]` : `[#${{String(paper.id).padStart(2, '0')}}]`;
      modalPaperNumBadge.textContent = `#${{String(paper.id).padStart(2, '0')}}`;
      modalCategoryTag.className = `category-tag theme-${{paper.category_theme || 'emerald'}}`;
      modalCategoryTag.textContent = paper.category || 'MBR';
      modalMetaYearJournal.textContent = `${{paper.year}} • ${{paper.journal_full || 'Peer-Reviewed Journal'}}`;
      modalPaperTitle.textContent = paper.title_vn || paper.title;
      modalPaperTitle.title = paper.title_en || paper.title;
      modalPaperSubtitle.textContent = paper.subtitle_vn || (paper.filter_tags || []).join(' • ');
      modalPaperAuthors.innerHTML = `
        <svg class="icon icon-xs" viewBox="0 0 24 24"><path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
        <span>${{paper.authors_full || paper.authors_short || ''}}</span>
      `;

      if (paper.branch_ready === false) {{
        modalLineageTag.innerHTML = `
          <svg class="icon icon-xs" viewBox="0 0 24 24" style="color: #ea580c;"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>
          <span style="color: #ea580c;">Cây Tri Thức Đang Xử Lý</span>
        `;
      }} else {{
        modalLineageTag.innerHTML = `
          <svg class="icon icon-xs" viewBox="0 0 24 24"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10"/><path d="m9 12 2 2 4-4"/></svg>
          <span>Đã Xác Thực Lineage</span>
        `;
      }}

      // Update PDF Buttons
      updatePdfButton(modalPdfOrigBtn, paper.pdf_original, 'Mở tệp PDF gốc tiếng Anh');
      updatePdfButton(modalPdfBilingualBtn, paper.pdf_bilingual, 'Mở tệp PDF song ngữ Việt - Anh');
      modalFigCountBadge.textContent = paper.figures || (paper.figures_list ? paper.figures_list.length : 0);

      // Handle Mindmap Pane
      if (paper.html_file) {{
        mindmapIframe.style.display = 'block';
        mindmapPlaceholder.style.display = 'none';
        mindmapIframe.src = `${{basePath}}${{paper.html_file}}`;
      }} else {{
        mindmapIframe.style.display = 'none';
        mindmapPlaceholder.style.display = 'block';
        mindmapPlaceholder.innerHTML = `
          <div class="tree-in-progress-notice">
            <h3>Cây tri thức đang được cập nhật</h3>
            <p>Bài báo <strong>[${{paper.pid}}] ${{paper.title_vn}}</strong> đang trong quá trình trích xuất cấu trúc tri thức.</p>
            <p>Bản dịch song ngữ toàn văn (VI-EN) đã sẵn sàng. Mở đọc trực tiếp theo nút bên dưới:</p>
            ${{paper.pdf_bilingual ? `
              <a class="btn-pdf bilingual" href="${{encodeURI(paper.pdf_bilingual)}}" target="_blank" style="padding: 9px 18px; font-size: 13px;">
                <svg class="icon icon-sm" viewBox="0 0 24 24"><path d="m5 8 6 6"/><path d="m4 14 6-6 2-3"/><path d="M2 5h12"/><path d="M7 2h1"/><path d="m22 22-5-10-5 10"/><path d="M14 18h6"/></svg>
                <span>Mở Bản Dịch Song Ngữ PDF (VI-EN)</span>
              </a>
            ` : ''}}
          </div>
        `;
      }}

      // Reset touch mode
      mindmapIframe.classList.remove('interactive');
      btnTouchToggle.textContent = 'Bật tương tác chạm';

      // Show Modal
      readerModalOverlay.classList.add('active');
      switchModalTab(defaultTab);
    }}

    function closeReaderModal() {{
      readerModalOverlay.classList.remove('active');
      document.body.style.overflow = '';
      mindmapIframe.src = '';
    }}

    modalCloseBtn.addEventListener('click', closeReaderModal);
    readerModalOverlay.addEventListener('click', (e) => {{
      if (e.target === readerModalOverlay) closeReaderModal();
    }});

    // Mobile Markmap Touch Trapping Toggle
    btnTouchToggle.addEventListener('click', () => {{
      const isInteractive = mindmapIframe.classList.toggle('interactive');
      btnTouchToggle.textContent = isInteractive ? 'Khóa để cuộn trang' : 'Bật tương tác chạm';
    }});

    // Helper: Configure PDF Buttons
    function updatePdfButton(btn, path, tooltip) {{
      if (path) {{
        btn.classList.remove('disabled');
        btn.href = encodeURI(path);
        btn.title = tooltip;
      }} else {{
        btn.classList.add('disabled');
        btn.removeAttribute('href');
        btn.title = 'Tài liệu chưa có sẵn trong kho lưu trữ cục bộ này';
      }}
    }}

    // Switch Modal View Tabs
    modalViewTabs.addEventListener('click', (e) => {{
      const tabBtn = e.target.closest('.modal-tab-btn');
      if (!tabBtn) return;
      switchModalTab(tabBtn.dataset.tab);
    }});

    function switchModalTab(tabKey) {{
      activeModalTab = tabKey;
      document.querySelectorAll('.modal-tab-btn').forEach(b => b.classList.toggle('active', b.dataset.tab === tabKey));
      
      const paneIds = {{
        mindmap: 'paneMindmap',
        tree: 'paneTree',
        gallery: 'paneGallery',
        benchmarks: 'paneBenchmarks'
      }};

      Object.entries(paneIds).forEach(([key, id]) => {{
        document.getElementById(id).classList.toggle('active', key === tabKey);
      }});

      // Update standalone URL link
      if (tabKey === 'mindmap') {{
        modalStandaloneBtn.href = activePaper.html_file ? `${{basePath}}${{activePaper.html_file}}` : '#';
      }} else if (tabKey === 'tree') {{
        modalStandaloneBtn.href = activePaper.md_file ? `${{basePath}}${{activePaper.md_file}}` : '#';
        loadMarkdownTree();
      }} else if (tabKey === 'gallery') {{
        modalStandaloneBtn.href = `${{basePath}}${{activePaper.slug}}/figures_manifest.json`;
        loadFiguresGallery();
      }} else if (tabKey === 'benchmarks') {{
        modalStandaloneBtn.href = `${{basePath}}${{activePaper.slug}}/RUN_REPORT.md`;
        loadBenchmarksReport();
      }}
    }}

    // Load Markdown Tree with Math (KaTeX) & Sticky TOC
    async function loadMarkdownTree() {{
      treeArticleInner.innerHTML = '<div style="padding: 40px; color: var(--text-muted); text-align: center;">Đang tải và render cấu trúc cây tri thức...</div>';
      treeTocList.innerHTML = '';

      if (!activePaper.md_file) {{
        treeArticleInner.innerHTML = `
          <div class="tree-in-progress-notice">
            <h3>Cây tri thức Markdown đang được xử lý</h3>
            <p>Bài báo <strong>[${{activePaper.pid}}] ${{activePaper.title_vn}}</strong> chưa có bản Markdown. Xem bản dịch song ngữ PDF (VI-EN) đầy đủ ở nút phía trên.</p>
          </div>
        `;
        return;
      }}

      try {{
        const mdUrl = `${{basePath}}${{activePaper.md_file}}`;
        const res = await fetch(mdUrl);
        if (!res.ok) throw new Error(`HTTP ${{res.status}}`);
        let mdText = await res.text();

        // Rewrite relative image paths to correct directory
        mdText = mdText.replace(/!\\[(.*?)\\]\\((assets\\/.*?)\\)/g, `![$1](${{basePath}}${{activePaper.slug}}/$2)`);

        // Parse markdown via marked.js
        treeArticleInner.innerHTML = marked.parse(mdText);

        // Auto-render LaTeX Equations via KaTeX
        if (window.renderMathInElement) {{
          renderMathInElement(treeArticleInner, {{
            delimiters: [
              {{left: "$$", right: "$$", display: true}},
              {{left: "\\\\[", right: "\\\\]", display: true}},
              {{left: "\\\\(", right: "\\\\)", display: false}},
              {{left: "$", right: "$", display: false}}
            ],
            throwOnError: false
          }});
        }}

        // Build Table of Contents
        const headings = treeArticleInner.querySelectorAll('h2, h3');
        headings.forEach((h, idx) => {{
          const id = `toc-heading-${{idx}}`;
          h.id = id;
          const a = document.createElement('a');
          a.className = `toc-item ${{h.tagName.toLowerCase() === 'h3' ? 'level-3' : 'level-2'}}`;
          a.textContent = h.textContent;
          a.href = `#${{id}}`;
          a.addEventListener('click', (evt) => {{
            evt.preventDefault();
            h.scrollIntoView({{ behavior: 'smooth', block: 'start' }});
          }});
          treeTocList.appendChild(a);
        }});
      }} catch (err) {{
        treeArticleInner.innerHTML = `
          <div style="padding: 30px; border: 1px solid var(--border); border-radius: 8px; background: var(--surface-elevated);">
            <h3 style="margin-bottom: 8px; color: var(--text);">Trình Duyệt Giới Hạn CORS Trực Tiếp</h3>
            <p style="color: var(--text-muted); font-size: 13px; margin-bottom: 14px;">Chính sách bảo mật file:// của trình duyệt giới hạn fetch cục bộ. Vui lòng mở tệp trực tiếp:</p>
            <p><a class="btn-action" target="_blank" href="${{basePath}}${{activePaper.md_file}}">Mở Tệp Markdown Độc Lập &nearr;</a></p>
          </div>
        `;
      }}
    }}

    // Load Figures & Tables Gallery
    function loadFiguresGallery() {{
      galleryGrid.innerHTML = '';
      const figs = activePaper.figures_list || [];
      if (figs.length === 0) {{
        galleryGrid.innerHTML = '<div style="color: var(--text-muted); padding: 40px; text-align: center; grid-column: 1/-1;">Không có dữ liệu đồ hình trích xuất cho mục này.</div>';
        return;
      }}
      figs.forEach((fig, index) => {{
        const card = document.createElement('div');
        card.className = 'fig-card';
        const imgUrl = `${{basePath}}${{activePaper.slug}}/${{fig.rel_path}}`;
        card.innerHTML = `
          <div class="fig-img-wrap">
            <img src="${{imgUrl}}" alt="Figure ${{fig.num}}" loading="lazy">
          </div>
          <div class="fig-card-body">
            <div class="fig-badge-row">
              <span class="fig-num-badge">Đồ Hình ${{fig.num}}</span>
              <span class="fig-page-info">Trang ${{fig.page}}</span>
            </div>
            <div class="fig-caption-text">${{fig.caption}}</div>
          </div>
        `;
        card.addEventListener('click', () => {{
          openLightbox(index);
        }});
        galleryGrid.appendChild(card);
      }});
    }}

    // Lightbox Modal Controls
    function openLightbox(index) {{
      const figs = activePaper.figures_list || [];
      if (index < 0 || index >= figs.length) return;
      currentLightboxIdx = index;
      const fig = figs[index];
      const imgUrl = `${{basePath}}${{activePaper.slug}}/${{fig.rel_path}}`;
      lightboxTitle.textContent = `Đồ Hình ${{fig.num}} (Trang ${{fig.page}}) — [${{index + 1}} / ${{figs.length}}]`;
      lightboxImg.src = imgUrl;
      lightboxCaption.textContent = fig.caption;
      lightboxModal.classList.add('active');
    }}

    function closeLightbox() {{
      lightboxModal.classList.remove('active');
    }}

    function navLightbox(delta) {{
      const figs = activePaper.figures_list || [];
      if (figs.length === 0) return;
      let nextIdx = currentLightboxIdx + delta;
      if (nextIdx < 0) nextIdx = figs.length - 1;
      if (nextIdx >= figs.length) nextIdx = 0;
      openLightbox(nextIdx);
    }}

    lightboxCloseBtn.addEventListener('click', closeLightbox);
    lightboxPrevBtn.addEventListener('click', () => navLightbox(-1));
    lightboxNextBtn.addEventListener('click', () => navLightbox(1));
    lightboxModal.addEventListener('click', (e) => {{
      if (e.target === lightboxModal) closeLightbox();
    }});

    // Load Benchmarks & Methodology Report
    async function loadBenchmarksReport() {{
      benchmarksContainer.innerHTML = '<div style="color: var(--text-muted); text-align: center; padding: 40px;">Đang tổng hợp thông số kỹ thuật và báo cáo kiểm định...</div>';
      const sum = activePaper.summary || {{}};

      let cardsHtml = `
        <div class="kpi-cards-grid">
          <div class="kpi-card">
            <div class="kpi-label">
              <svg class="icon icon-xs" viewBox="0 0 24 24"><rect width="18" height="18" x="3" y="3" rx="2" ry="2"/><line x1="3" x2="21" y1="9" y2="9"/><line x1="9" x2="9" y1="21" y2="9"/></svg>
              <span>Miền Ứng Dụng & Quy Mô</span>
            </div>
            <div class="kpi-val">${{sum.domain || 'Xử lý nước thải & Công nghệ màng'}}</div>
            <div class="kpi-sub">${{sum.scale || 'Quy mô công nghiệp / Pilot'}}</div>
          </div>

          <div class="kpi-card">
            <div class="kpi-label">
              <svg class="icon icon-xs" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><line x1="12" x2="12" y1="6" y2="12"/><line x1="12" x2="16" y1="12" y2="16"/></svg>
              <span>Thông Số Mục Tiêu</span>
            </div>
            <div class="kpi-val">${{sum.target_variables || sum.target || 'Chỉ số hiệu suất vận hành KPI'}}</div>
            <div class="kpi-sub">Biến trạng thái vật lý dự báo</div>
          </div>

          <div class="kpi-card">
            <div class="kpi-label">
              <svg class="icon icon-xs" viewBox="0 0 24 24"><polygon points="12 2 2 7 12 12 22 7 12 2"></polygon><polyline points="2 17 12 22 22 17"></polyline><polyline points="2 12 12 17 22 12"></polyline></svg>
              <span>Thuật Toán Học Máy (AutoML)</span>
            </div>
            <div class="kpi-val">${{sum.algorithms || sum.models || 'Mô hình học máy benchmark'}}</div>
            <div class="kpi-sub">Lựa chọn & tối ưu hóa siêu tham số</div>
          </div>

          <div class="kpi-card">
            <div class="kpi-label">
              <svg class="icon icon-xs" viewBox="0 0 24 24"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg>
              <span>Độ Chính Xác Thực Nghiệm</span>
            </div>
            <div class="kpi-val" style="color: var(--accent-bio);">${{sum.metrics || 'Kiểm định chéo hold-out'}}</div>
            <div class="kpi-sub">Chỉ số đánh giá định lượng sai số</div>
          </div>

          <div class="kpi-card" style="grid-column: 1 / -1;">
            <div class="kpi-label">
              <svg class="icon icon-xs" viewBox="0 0 24 24"><circle cx="11" cy="11" r="8"/><line x1="21" x2="16.65" y1="21" y2="16.65"/></svg>
              <span>Đóng Góp Đặc Trưng & Cơ Chế Vật Lý (XAI)</span>
            </div>
            <div class="kpi-val" style="font-size: 13.5px; font-weight: 500; line-height: 1.55;">${{sum.key_insights || sum.shap || 'Giải thích quy luật vận hành vật lý'}}</div>
          </div>
        </div>
      `;

      try {{
        const reportUrl = `${{basePath}}${{activePaper.slug}}/RUN_REPORT.md`;
        const res = await fetch(reportUrl);
        if (!res.ok) throw new Error(`HTTP ${{res.status}}`);
        const reportMd = await res.text();
        const reportHtml = marked.parse(reportMd);

        benchmarksContainer.innerHTML = `
          ${{cardsHtml}}
          <div class="report-box">
            <h2>Hồ Sơ Nguồn Gốc & Quá Trình Tổng Hợp (Pipeline Lineage Record)</h2>
            ${{reportHtml}}
          </div>
        `;
      }} catch (err) {{
        benchmarksContainer.innerHTML = `
          ${{cardsHtml}}
          <div class="report-box">
            <h2>Hồ Sơ Nguồn Gốc & Quá Trình Tổng Hợp (Pipeline Lineage Record)</h2>
            <p style="color: var(--text-muted); font-size: 13px; margin-bottom: 12px;">Truy cập trực tiếp báo cáo tổng hợp:</p>
            <p><a class="btn-action" target="_blank" href="${{basePath}}${{activePaper.slug}}/RUN_REPORT.md">Mở RUN_REPORT.md &nearr;</a></p>
          </div>
        `;
      }}
    }}

    // View Mode Toggle (Grid vs List)
    viewGridBtn.addEventListener('click', () => {{
      currentViewMode = 'grid';
      viewGridBtn.classList.add('active');
      viewListBtn.classList.remove('active');
      researchGrid.classList.remove('list-view');
    }});

    viewListBtn.addEventListener('click', () => {{
      currentViewMode = 'list';
      viewListBtn.classList.add('active');
      viewGridBtn.classList.remove('active');
      researchGrid.classList.add('list-view');
    }});

    // Live Search Handling (Tab 1)
    searchInput.addEventListener('input', (e) => {{
      searchQuery = e.target.value.trim();
      searchClearBtn.classList.toggle('active', searchQuery.length > 0);
      renderLibrary();
    }});

    searchClearBtn.addEventListener('click', () => {{
      searchInput.value = '';
      searchQuery = '';
      searchClearBtn.classList.remove('active');
      searchInput.focus();
      renderLibrary();
    }});

    // Live Search Handling (Tab 2 Extended)
    extSearchInput.addEventListener('input', (e) => {{
      extSearchQuery = e.target.value.trim();
      renderExtendedTable();
    }});

    // Filter Chips Handling (Tab 1)
    filterChipsRow.addEventListener('click', (e) => {{
      const chip = e.target.closest('.filter-chip');
      if (!chip) return;
      document.querySelectorAll('.filter-chip').forEach(c => c.classList.remove('active'));
      chip.classList.add('active');
      currentFilter = chip.dataset.filter;
      
      const filterNames = {{
        all: 'Tài liệu y văn 2018–2026',
        automl: 'Chủ đề: AutoML & AI Giải Thích (XAI)',
        mbr: 'Chủ đề: Công Nghệ Lọc Màng Sinh Học (MBR)',
        anammox: 'Chủ đề: Xử Lý Nitơ Bằng Vi Sinh Anammox',
        transfer: 'Chủ đề: Học Chuyển Giao (Transfer Learning)',
        review: 'Chủ đề: Tổng Quan & Cẩm Nang Nghiên Cứu',
        water_quality: 'Chủ đề: Giám Sát & Xử Lý Nước Cấp'
      }};
      filterStatusText.textContent = filterNames[currentFilter] || '';
      renderLibrary();
    }});

    // Fullscreen Toggle
    modalFullscreenBtn.addEventListener('click', () => {{
      if (!document.fullscreenElement) {{
        readerModalOverlay.requestFullscreen().catch(() => {{}});
      }} else {{
        document.exitFullscreen().catch(() => {{}});
      }}
    }});

    // Global Keyboard Shortcuts (Esc for modals, Left/Right for lightbox)
    document.addEventListener('keydown', (e) => {{
      if (lightboxModal.classList.contains('active')) {{
        if (e.key === 'Escape') closeLightbox();
        else if (e.key === 'ArrowLeft') navLightbox(-1);
        else if (e.key === 'ArrowRight') navLightbox(1);
      }} else if (readerModalOverlay.classList.contains('active')) {{
        if (e.key === 'Escape') closeReaderModal();
      }}
    }});

    // Theme Engine (Dark / Light)
    const savedTheme = localStorage.getItem('hub-theme') || 'dark';
    document.documentElement.setAttribute('data-theme', savedTheme);
    updateThemeIcon(savedTheme);

    themeToggleBtn.addEventListener('click', () => {{
      const current = document.documentElement.getAttribute('data-theme') || 'dark';
      const target = current === 'dark' ? 'light' : 'dark';
      document.documentElement.setAttribute('data-theme', target);
      localStorage.setItem('hub-theme', target);
      updateThemeIcon(target);
    }});

    function updateThemeIcon(theme) {{
      if (theme === 'dark') {{
        themeToggleIcon.innerHTML = '<circle cx="12" cy="12" r="5"/><line x1="12" y1="1" x2="12" y2="3"/><line x1="12" y1="21" x2="12" y2="23"/><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/><line x1="1" y1="12" x2="3" y2="12"/><line x1="21" y1="12" x2="23" y2="12"/><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/>';
      }} else {{
        themeToggleIcon.innerHTML = '<path d="M12 3a6 6 0 0 0 9 9 9 9 0 1 1-9-9Z"/>';
      }}
    }}

    // Initial Mount
    renderLibrary();
    renderExtendedTable();
  </script>
</body>
</html>
'''

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_template)

with open('branche_v2/index.html', 'w', encoding='utf-8') as f:
    f.write(html_template)

print(f"Generated index.html and branche_v2/index.html successfully!")
print(f"Tab 1 Core Papers: {len(catalog_30)}")
print(f"Tab 2 Extended Papers: {len(extended_65)}")
