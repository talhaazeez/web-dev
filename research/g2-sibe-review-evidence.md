# G2 and official Sibe review evidence

## G2 reviews

Source: https://www.g2.com/products/sibe/reviews

The publicly extracted G2 page contains two review passages from one visible reviewer profile, Jessica C. The first describes simplified file management, change tracking, clear version control, cloud setup, and browser-based access for external partners and non-technical team members. The second describes the overall experience as positive while noting that notification controls and alert consistency could be improved. Both passages are labeled as collected and hosted on G2.com.

The extracted page did not expose a numeric aggregate rating, review count, vote count, review date, or a product screenshot suitable for `SoftwareApplication.screenshot`.

## Official Sibe product page

Source: https://www.sibe.io/

The official product page describes a 14-day free trial, no credit card requirement, quick setup, SolidWorks version control, check-in/check-out, version history, browser-based sharing, and a demo with Ken Maren. It also provides first-party product images and customer testimonial content, but those assets are not automatically reused in structured data without a local, stable screenshot asset.

## Schema decision

Use the G2 URL as an `sameAs` review-profile link for the Sibe software entity and cite the review page in visible homepage copy if desired. Do not add `aggregateRating`, `ratingValue`, `reviewCount`, `upvoteCount`, or `suggestedAnswer` without explicit public values from the source. Do not use a logo or testimonial portrait as a `SoftwareApplication.screenshot`; a screenshot must depict the software interface.

## Browser-visible G2 facts

The rendered G2 page title is “Sibe Reviews 2026: Details, Pricing, & Features | G2.” The visible product summary shows an aggregate rating of 4.9/5 based on 35 reviews. The page also shows one visible review by Jessica C., dated 8/14/2026, with a 5/5 score. The review describes clearer cloud version control, browser access for external partners and non-technical team members, and fewer file-sharing errors; it also notes that notification controls and alert consistency could be improved.

The visible G2 page presents product branding and a profile-style product card, not a software-interface screenshot. The G2 URL is suitable as a review-profile `sameAs` link and as the source for a visible review-context link. The rating and review count are suitable only if represented as an external review aggregate with the G2 source URL and kept current.
