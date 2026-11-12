# iRana Cams - App Store Connect draft

Use the fields below as a starting point for the first App Store listing. Verify
the final copy, privacy answers, age rating, and availability in App Store
Connect before submission.

## Store metadata

**App name**  
`iRana Cams – IP Camera Viewer`

**Subtitle**  
`ONVIF, RTSP Live Grid & PTZ`

**Promotional text**  
Watch compatible ONVIF and RTSP cameras live, organize views into dashboards,
and use PTZ controls when your camera supports them.

**Description**

Keep your compatible IP cameras close at hand with iRana Cams.

WATCH LIVE VIDEO

- Add compatible ONVIF cameras or enter an RTSP stream.
- View saved cameras in a list or grid, then open a feed full screen.
- Switch between saved cameras while watching.
- Play supported H.264 and H.265 streams over TCP or UDP.

MAKE A DASHBOARD

- Group and arrange cameras in saved dashboards.
- View up to nine streams at once, depending on your device and network.

CONTROL SUPPORTED CAMERAS

- Use pan, tilt, zoom, and presets when a camera exposes compatible ONVIF controls.

SAVE IMPORTANT MOMENTS

- Capture snapshots and record MP4 clips.
- Keep captures in the app or choose to save them to Photos.

BUILT-IN DEMO MODE

Explore simulated cameras, dashboards, and controls without connecting a physical camera.

PRIVACY AND SYNC

- Camera video connects directly to your device; iRana Labs does not operate a video relay.
- Optional iCloud sync is off by default and stores camera configuration in your private iCloud database.
- Camera passwords are kept in Apple Keychain and are not stored in CloudKit records.
- Uploading snapshots to iCloud requires a separate opt-in.

Camera compatibility depends on firmware, stream configuration, and network.
Some discovery may be limited by router or subnet settings; cameras can also be
added manually. Audio and PTZ capabilities vary by camera.

**Keywords**  
`onvif,rtsp,security camera,ptz,nvr,live video,home camera,network camera,video`

**What's New**  
First release of iRana Cams.

## URLs

- Marketing URL: `https://iranalabs.com/apps/irana-cams/`
- Support URL: `https://iranalabs.com/apps/irana-cams/support/`
- Privacy Policy URL: `https://iranalabs.com/apps/irana-cams/privacy/`

These URLs are drafts until the website is deployed and verified publicly.

## Review information

Suggested App Review Notes:

> iRana Cams can be reviewed without a physical camera. Complete onboarding,
> open Settings > Demo Mode, and enable it. Return to Cameras and open any demo
> camera. Demo discovery, streams, and PTZ are simulated.

## Suggested listing setup

- Primary category: Utilities (confirm this fits the final listing).
- Copyright: `2026 iRana Labs` (use the correct legal rights holder).
- Complete the age-rating questionnaire from the app's actual content and controls.
- Review App Privacy answers against the published policy and `PrivacyInfo.xcprivacy`.
- Complete export-compliance questions in App Store Connect; the project currently
  declares `ITSAppUsesNonExemptEncryption = NO`.
- Add iPhone and iPad screenshots from `site/assets/screenshots/`. They use
  genuine app screens captured in Demo Mode; the app marks its feeds as
  simulated and the product page says so. Replace the source captures with real
  camera footage if you prefer that for the final storefront.

## App Privacy draft

The current `PrivacyInfo.xcprivacy` declares these data types as linked to the
user, used for App Functionality, and not used for tracking:

| App Store Connect data type | Current manifest entry | Suggested answers |
|---|---|---|
| Other User Content | `NSPrivacyCollectedDataTypeOtherUserContent` | Linked to the user: Yes; used for tracking: No; purpose: App Functionality |
| Photos or Videos | `NSPrivacyCollectedDataTypePhotosorVideos` | Linked to the user: Yes; used for tracking: No; purpose: App Functionality |

Use those declarations as the starting point for the App Privacy questionnaire.
The app's optional private CloudKit sync and snapshot uploads are user-enabled;
confirm the final collection answers against Apple's current definition and the
data flows in the release build before publishing the label. Do not select
"No, we do not collect data" without reconciling that answer with the manifest.
No advertising or analytics tracking is declared by the app.

## Screenshot targets

Apple currently requires an iPhone screenshot for an iPhone with Dynamic Island
and a 13-inch iPad screenshot for apps that support iPadOS. These captures target
the required Dynamic Island medium iPhone and 13-inch iPad sizes:

- iPhone 18 Pro portrait: 1206 x 2622 pixels
- iPad portrait: 2064 x 2752 pixels

The generated assets are `01-cameras.jpg`, `02-dashboard.jpg`, and
`03-live-view.jpg` in each device folder.

Confirm the current App Store Connect screenshot specifications when uploading.
