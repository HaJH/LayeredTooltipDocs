### ILayeredTooltipWidget API Reference

> Interface for custom tooltip widgets.

#### Interface Declaration

```cpp
UINTERFACE(MinimalAPI)
class ULayeredTooltipWidget : public UInterface
{
    GENERATED_BODY()
};

class LAYEREDTOOLTIP_API ILayeredTooltipWidget
{
    GENERATED_BODY()
public:
    virtual FOnTooltipDestroyDelegate& GetOnTooltipDestroyDelegate() = 0;
    FString TriggerId; // Set automatically by the tooltip system
};
```

#### Functions

##### InitializeLayeredTooltip

```cpp
UFUNCTION(BlueprintCallable, BlueprintNativeEvent, Category = "LayeredTooltip")
void InitializeLayeredTooltip(const FLayeredToolTipTriggerData& TriggerData);
```

- **Called:** Once when tooltip is created
- **Parameters:** `TriggerData` - Trigger configuration data

##### SetLayeredTooltipTitle

```cpp
UFUNCTION(BlueprintCallable, BlueprintNativeEvent, Category = "LayeredTooltip|Text")
void SetLayeredTooltipTitle(const FText& InText);
```

- **Purpose:** Set main title text
- **Parameters:** `InText` - Title text

##### SetLayeredTooltipText

```cpp
UFUNCTION(BlueprintCallable, BlueprintNativeEvent, Category = "LayeredTooltip|Text")
void SetLayeredTooltipText(const FText& InText);
```

- **Purpose:** Set main body text
- **Parameters:** `InText` - Body text

##### GetLayeredTooltipTitle

```cpp
UFUNCTION(BlueprintCallable, BlueprintNativeEvent, Category = "LayeredTooltip|Text")
FText GetLayeredTooltipTitle();
```

- **Returns:** Current title text

##### GetLayeredTooltipText

```cpp
UFUNCTION(BlueprintCallable, BlueprintNativeEvent, Category = "LayeredTooltip|Text")
FText GetLayeredTooltipText();
```

- **Returns:** Current body text

##### OnLayeredTooltipPinned

```cpp
UFUNCTION(BlueprintCallable, BlueprintNativeEvent, Category = "LayeredTooltip|Pinned")
void OnLayeredTooltipPinned(bool bPinned);
```

- **Called:** When pin state changes
- **Parameters:** `bPinned` - Pin state

##### OnLayeredTooltipStartTimer

```cpp
UFUNCTION(BlueprintCallable, BlueprintNativeEvent, Category = "LayeredTooltip|Pinned")
void OnLayeredTooltipStartTimer(float Time);
```

- **Called:** To show countdown timer
- **Parameters:** `Time` - Timer duration in seconds

##### OnLayeredTooltipStopTimer

```cpp
UFUNCTION(BlueprintCallable, BlueprintNativeEvent, Category = "LayeredTooltip|Pinned")
void OnLayeredTooltipStopTimer();
```

- **Called:** To hide countdown timer

##### GetOnTooltipDestroyDelegate

```cpp
virtual FOnTooltipDestroyDelegate& GetOnTooltipDestroyDelegate() = 0;
```

- **Returns:** Reference to destroy delegate
- **Note:** Pure virtual function

#### Delegate Type

```cpp
DECLARE_MULTICAST_DELEGATE_OneParam(FOnTooltipDestroyDelegate, const FString&);
```

#### Base Implementation

```cpp
UCLASS(Abstract, Blueprintable)
class LAYEREDTOOLTIP_API ULayeredTooltipUserWidget : public UUserWidget, public ILayeredTooltipWidget
{
    GENERATED_BODY()
public:
    virtual void NativeConstruct() override;
    virtual FOnTooltipDestroyDelegate& GetOnTooltipDestroyDelegate() override;
    virtual FText GetLayeredTooltipText_Implementation() override;
    
protected:
    virtual void NativeDestruct() override;
    FOnTooltipDestroyDelegate OnTooltipDestroy;
};
```