# Questions for Product Owner

Add questions below as bullet points. The product owner should reply directly beneath each item.
Once the information has been integrated into the repo (docs or code), remove the entry.

- **Q:** For the Dexcom API connector, which OAuth grant flow and API scopes should we implement?
  **A:** _TBD_ On hold for now.
- **Q:** Should Nightscout imports support both treatments and sensor glucose endpoints?
  **A:** Yes include both. Be aware that nightscout only logs bolus and not basal insulin. Have an option to set basal manually.
- **Q:** Do we have target thresholds for the overnight basal drift detector (e.g. mmol rise over 4 h)?
  **A:** No fixed targets. The solution should calculate the overnight drift in several consecutive days and use that to determine a trend. E.g., is the BG regularly increasing by 2 mmol/L over 4 hours overnight? This should be a simple stastical model that considers variance. The number of days to consider should be a variable. Conclusion on basal drift should not be based on single observations.
- **Q:** When tagging exercise from Fitbit/Google Fit, what step-count thresholds classify moderate versus vigorous activity?
  **A:** _TBD_
- **Q:** For the linear BG prediction prototype, what error metric and acceptable accuracy define success?
  **A:** Please modify the question where you write your recommendation with a reason. Then I'll update the answer.
