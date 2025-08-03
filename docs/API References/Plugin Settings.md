---
sidebar_position: 2
---
> You can manage overall plugin settings in `Project Settings → Plugins → LayeredTooltip Settings`.

#### Essential Settings for Basic Use

**Tooltip Display Delay**

- **Default:** `0.1 seconds`
- **Purpose:** Time for tooltip to appear on mouse hover

**Tooltip Position Offset**

- **Default:** `(4, 4)`
- **Purpose:** Distance from mouse cursor to tooltip

#### Advanced Settings for Customization

**Layered Tooltip Widget Class**

- **Default:** Plugin default widget
- **Requirements:** Must implement `ILayeredTooltipWidget` interface

**Tooltip Text Provider Class**

- **Default:** Uses string table
- **Requirements:** Must implement `ILayeredTooltipTextProvider` interface

**Default Tooltip Text String Table**

- **Default:** Plugin default string table

#### Settings for Advanced Users

**Tooltip Tags**

- **Default:** `["Tooltip"]`
- **Purpose:** Add tag names for use in rich text
- **Example:** `["tooltip", "help", "item"]` → Enables `<tooltip>`, `<help>`, `<item>` tags

**Tooltip Pin Delay**

- **Default:** `1.0 seconds`
- **Purpose:** Time until tooltip becomes pinned and clickable
- **Adjustment:** Longer prevents accidental pinning; shorter enables quick interaction

**Tooltip Default Z Order**

- **Default:** `1000`
- **When to Adjust:** Set higher value when tooltip is hidden behind other UI elements

#### Debug Settings

**Layered Tooltip Debug**

- **Default:** `false`
- **When Enabled:** Shows tooltip trigger areas and outputs detailed logs
- **Purpose:** Diagnose issues when tooltips don't work

#### Important Notes

- Editor restart may be required when changing widget/text provider classes.