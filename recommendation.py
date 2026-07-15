def generate_recommendations(patient):

    recommendations = []

    diseases = patient["diseases"].lower()
    allergies = patient["allergies"].lower()

    if "hypertension" in diseases:
        recommendations.append("🩺 Monitor blood pressure every month.")
        recommendations.append("🥗 Reduce salt intake.")

    if "diabetes" in diseases:
        recommendations.append("🩸 Check blood sugar regularly.")
        recommendations.append("🍎 Follow a diabetic-friendly diet.")

    if "heart disease" in diseases:
        recommendations.append("❤️ Schedule ECG every 6 months.")
        recommendations.append("🚶 Maintain regular physical activity.")

    if "migraine" in diseases:
        recommendations.append("💊 Track headache frequency and triggers.")

    if "asthma" in diseases:
        recommendations.append("🌬 Carry inhaler and avoid dust exposure.")

    if "penicillin" in allergies:
        recommendations.append("⚠ Avoid Penicillin.")

    if "nuts" in allergies:
        recommendations.append("⚠ Avoid nuts and nut-based food.")

    recommendations.append("✅ Continue prescribed medications.")
    recommendations.append("📅 Schedule regular follow-up visits.")

    return recommendations