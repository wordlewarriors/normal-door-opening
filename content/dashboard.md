# 📊 Campaign Dashboard
> Use this dashboard to explore the Wordle Warriors campaign using Dataview.
---

## 📅 Recent Sessions
```dataview
TABLE date, arc, themes, locations
FROM "Sessions"
SORT date desc
LIMIT 10
```

## 📖 Sessions by Arc
```dataview
TABLE session, date, locations, themes
FROM "Sessions"
GROUP BY arc
SORT date
```

## 🧙 Character-Focused Sessions (e.g. Jorund)
```dataview
TABLE session, date, arc, themes
FROM "Sessions"
WHERE contains(tags, "jorund")
SORT date
```

## 🧪 Sessions Involving the Plague
```dataview
TABLE session, date, arc, npcs, locations
FROM "Sessions"
WHERE contains(themes, "plague")
SORT date
```

## 🔮 Soul Trial Progress
```dataview
TABLE session, date, characters, themes
FROM "Sessions"
WHERE contains(themes, "soultrial")
SORT date
```

## 🧭 Sessions Set in Neverwinter
```dataview
TABLE session, date, arc, npcs
FROM "Sessions"
WHERE contains(locations, "Neverwinter")
SORT date
```

## 📌 Sessions by Year
```dataview
TABLE session, arc, locations, themes
FROM "Sessions"
GROUP BY date.year
SORT date
```

---
_Last updated: 22 July 2025_
