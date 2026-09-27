# Scoping evidence: the opening exchanges of all 72 selected cases

Extracted automatically with cases2.py (first page of each case). I = interviewer; C? = the candidate's clarifying questions.

```
### Product design | Credit platform for teenagers
  I: Problem Statement - Create a fintech platform for credit for teenagers.
  I: Sure, that’s a fair point. So how would describe your target segment?
  I: This looks good. You may proceed with the features.
  I: Great. And are there any features you would add for the guardian’s persona?
### Product design | Bank app for rural India
  I: You’re a Product Manager for X Bank in India. Design a mobile application catering to Rural India.
  C?: Before we move forward, I have a few clarifying questions: Do we assume that the bank already has KYC-authenticated customers in rural India and we want to enable e-services? | In which geographies does our bank operate? | How does the consumer currently use services of our bank/ other banks? | Is there a particular objective behind launching the app?
  I: You may assume that the bank already has a vast rural customer base across India. Currently the bank offers its services only through its branches, however due to lack of infrastructure in many rural areas, the branches 
  C?: Customers availing services can be broadly classified in 2 types: • Vendors • Regular Customers Is there a particular category of users you would like me to explore?
  I: You’re free to choose and proceed.
  C?: Am I missing anything or is there a particular issue faced by the customers which you would want me to explore?
  I: This seems to be apt. Please proceed with your analysis.
### Product improvement | Improve your favourite UPI app
  I: What is your favourite UPI application and how would you improve it? (AppDynamics)
  I: What would be the main differentiators for PhonePe?
  C?: Can I now proceed with analyzing how they can improve their product?
  I: Yes, please proceed.
  C?: I would like to know what is the goal of the app improvement? | Improving user engagement, increasing market share, increasing user retention or increase revenue?
  I: What is the most pressing issue in the payments space according to you?
### Product improvement | Fraud prevention in a mobile banking app
  I: Can you improve the IDFC Bank mobile app for preventing frauds
  I: You can assume the app to be a standard mobile banking app like IDFC bank. We are looking at frauds during any transactions. There is no constraint on the region since the app is used pan – India.
  C?: Are there any metrics that we are targeting to improve?
  I: You may proceed. What metrics should we target according to you.
  C?: Do we have any user personas in mind or should I come up with them?
  I: Sounds good. You can come up with user personas.
### Metrics | Promotions in Google Pay
  I: You are a product manager in the Google Pay team. You have been given the task of defining the metrics for tie-in promotions on Google Pay. How will you go about it?
  C?: Is that accurate?
  I: Your description of tie-in promotions is accurate. Essentially tie-in promotions involve a company partnership with another company for promotions. You can proceed further with your analysis.
  I: The business goals seem accurate. Please proceed with the metrics.
### Root cause analysis | Android DAU drop in a banking app
  I: You’re the PM for our mobile banking app. Android Daily Active Users (DAU) fell 40% in the last two weeks while iOS DAU stayed steady. Walk me through how you’d diagnose the root cause.
  C?: Correct?
  I: Yes, that's correct.
  C?: Is DAU unique users who opened the app at least once that day? | Is the drop across both new and existing users? | And is it global or localised?
  I: Yes, unique daily users. Both new and existing are hit. It’s global but more pronounced in North America.
  C?: First, metric reliability - any change to analytics tooling or event definitions, or any processing delay or mis-aggregation?
  I: No changes, and no delays or aggregation errors.
### Product design | Quick-commerce vendor management
  I: Our quick commerce platform works with thousands of vendors. Today, purchase orders, shipment updates and invoices flow through a mix of EDI integrations, emails and spreadsheets, making procurement inefficient. As the P
  C?: Can I clarify a few things? | Will this platform be used only by our internal procurement teams, or will vendors also have • access? | Are we replacing existing procurement systems or building a layer that integrates with existing • ERPs and EDI systems? | What is the primary business goal - reducing operational effort, improving inventory availability, • or improving vendor collaboration?
  I: Good questions. The platform will be used by both procurement teams and vendors. We're not replacing ERPs like SAP. Instead, we're building a collaboration layer that integrates with existing ERP and EDI systems. The pri
  C?: Does that approach sound good?
  I: Yes, please go ahead.
### Product improvement | Improve Swiggy
  I: We would like you to pick a food delivery app and focus on improving it. (Infoedge)
  I: That was comprehensive. Please proceed further.
  C?: Is there a specific goal I should be able to achieve through the improvement features?
  I: No, you are free to define the goal.
  C?: I would want to focus on end consumers, will that be okay?
  I: Sure. Please proceed.
### Metrics | BigBasket success metrics
  I: You are the Digital Product Manager of Big Basket. What would be the metrics you would like to follow?
  I: Yes, you may move forward.
  C?: Before defining metrics, could you share the business goal we'd like to measure?
  I: Assume that the goal of the business is to increase the value of orders placed via the BigBasket mobile app.
  C?: Should I cover both the website and the mobile app?
  I: You can define the metrics for only the mobile app for now.
### Metrics | Swiggy: product metrics before an IPO
  I: You are the CPO of Swiggy, what key product metrics would you monitor in preparation for an IPO?
  C?: Does this sound reasonable, should I proceed and list the metrics?
  I: Yes, please proceed. Also, include the rationale behind selecting each metric, particularly in the context of the upcoming IPO.
  I: It was a comprehensive list. How would you use these metrics to prepare for the IPO?
### Go-to-market | Swiggy table reservations launch
### Root cause analysis | Zomato cancellations rise
  I: We’ve seen 4-5% increase in customer initiated cancellations in the last few weeks. How would you approach this problem?
  C?: Is the increase seen across the entire customer base, or is it concentrated in specific cities or customer segments?
  I: It’s mainly in major metros and among frequent users.
  C?: And at what stage are customers cancelling? | Before the restaurant starts prepping, or later in the process?
  I: Mostly before preparation begins.
  C?: Are we aware whether this spike is recent or if cancellations have been trending upward over time? | Or have we shipped any new feature recently?
  I: Spike is recent in last 2-3 weeks, and no major product changes
### Root cause analysis | Zepto delivery-time breaches
  I: Zepto in Bangalore is observing breaches. Can you please diagnose the issue?
  C?: What do we mean by breaches here? | How do we measure these breaches at Zepto?
  I: For Zepto, we measure average delivery time per order. We are seeing a rise in the same.
  C?: How much is the rise observed in average delivery time per order?
  I: We are seeing about 25% increase in the delivery times.
  C?: What categories are we observing these breaches in? | or across all categories?
  I: The rise is seen across all categories.
### Product design | E-commerce for senior citizens
  I: How would you design an e-commerce platform for senior citizens? (Flipkart)
  C?: Firstly, are we building a new ecommerce platform from scratch or are we making changes to an existing one? | Secondly, how do we define a ‘senior citizen’?
  I: We already have an e-commerce platform. We have a website as well as apps for Android and iOS. Senior citizens are folks above the age of 60.
  I: I think that’s a fair assessment. You can go ahead with this.
  C?: Do we have any platform specific usage data on senior citizens?
  I: Close to 90% of our users above 60 are on Android. Your logic sounds good! Let’s go ahead with Android.
### Product improvement | AI for Myntra's app
  I: You are a Product Manager at Myntra. The leadership believes that Artificial Intelligence (AI) is the key to the next phase of growth. How would you leverage AI to significantly increase customer engagement on the app?
  C?: When we say "leverage AI," are we looking at Generative AI (like chatbots/image generation), Predictive AI (recommendations), or Computer Vision? | Or am I free to explore the best fit?
  I: You are free to explore the best fit, but the primary goal remains increasing engagement (daily active usage and session time), not just transaction volume
  I: Sounds good. Let's start with the personas
  C?: Often thinks, "I have this skirt, but what do I wear with it?" They need a Stylist. | If we use AI to solve their "styling" problem using their existing purchases, we create a daily use case ("What do I wear today?") rather than just a shopping use case.
  I: That’s a strong choice. Solving the "post-purchase" or "pre-wear" anxiety is a great engagement hook. What AI solutions do you propose?
### Metrics | Facebook Marketplace metrics
  I: You are the PM for Facebook Marketplace. What metrics would you track to measure the health and success of the feature?
  I: You are right. Please go ahead.
  I: Your understanding of the journey of the stakeholders is fair. Let’s move ahead to the metrics
  I: Alright, out of all these metrics mentioned, which one should be prioritized by us as the top metric?
### Root cause analysis | Decline in cart additions
  I: There’s a roughly 10% decline in cart additions (Add to Bag) over the last three days on Myntra. Can you help investigate?
  C?: Correct?
  I: Yes, that is correct.
  C?: Is the 10% drop across all platforms, or specific to one?
  I: It’s on the Myntra Android app.
  C?: Across all product categories or specific ones?
  I: Across all categories. Yes, you may assume that.
### Root cause analysis | Amazon return rate rises
  I: There has been increase in the return-rate for Amazon products. What can be done?
  C?: Is the decline sudden or gradual? | Does the decline occur during any particular season?
  I: The increase has been gradual. But, the return-rate peaks during the wedding/festive season.
  C?: Is there any specific product category for which the return-rate is increasing much?
  I: Return rates of Clothes and Electronics have increased the most. You can focus on clothes for now.
  C?: Is this problem prevalent across India or is it specific to some particular geographic locations?
  I: We are facing this issue across India.
### Pricing | Amazon Prime: price-cut projection
  I: Assume you are the new product manager in our Amazon Prime business and are deciding pricing. The vice president would like to lower the price from $99.99 per year to $89.99 per year. Making your own assumptions, develop
  I: So, what’s the overall change in revenue, and what’s your recommendation?
### Pricing | Pricing Amazon Prime
  I: How would you price Amazon Prime?
  C?: Am I correct with this?
  I: Yes, you are correct.
  C?: Are we focusing on any specific geography for this decision?
  I: We are focusing on India.
  C?: Got it! Are we aiming to maximize our market share, or are we focusing on maximizing our profits with this pricing strategy?
  I: Our goal is to attract more customers and boost our market share.
### Pricing | Vendor price negotiation
  I: Hi, you are a product manager at a popular cloud services company. Your main product is a platform that provides on-demand GPU instances for AI startups and researchers to train their models. You source your capacity fro
  I: Go ahead.
  C?: I would like to understand what kind of pricing structure is currently in place, and what is the reason for which the vendor is asking for the renegotiation?
  I: Currently, we have a pay-per-use payment model. Here, the amount to be paid per user depends on the band in which the lump sum requirements of the GPU server's capacity lie. Recently, a major new open-source AI model was
  C?: Which one has been the case with us?
### Strategy | Stopping fake products on Instagram
  I: How to stop fake product selling on Instagram?
  C?: First, What types of fake products are most commonly sold on Instagram, and is there any existing system in place to combat fake product selling?
  I: Let’s say clothing accessories and there is no existing system.
  C?: One more clarifying question, What is the primary goal for Instagram in addressing this issue? | Is it user trust, legal compliance, or revenue protection?
  I: You are free to decide.
  C?: Is that acceptable?
  I: Sure, please proceed.
### Product design | Ola for schoolkids
### Product design | Uber for kids
  I: Uber wants to get into the business of pooled - student commuting in US. How would you go about with the product design?
  C?: Does that sound good to you?
  I: Sounds good, please proceed.
  C?: Before I proceed, can I know whether children below the age of 18 are allowed to have an Uber account?
  I: For the purpose of this case, you can assume that children can have an account linked to their parents.
  C?: Also, what is the age group Uber is looking to target?
  I: You can take kids upto grade 7.
### Product improvement | Improve Uber
  I: Improve the Product Design for Uber (Adobe)
  C?: Before we start, Is it OK if I have some few questions?
  I: Sure. Please go ahead.
  C?: What is the market we are operating in?
  I: You can assume we are operating in India only.
  I: Fair Assumption. Please go ahead .
### Product improvement | Improve Google Maps
  I: How would you improve Google Maps? (VMock)
  C?: What do you mean when you say improve? | Is the goal to enhance engagement, acquire more users, or to generate more revenue?
  I: Let’s go with engagement
  C?: Sure, and do we have any specific platform in mind? | iOS app, Android app, or website? | Or is it across all platforms?
  I: Around 80% of our users are on Android so let’s start with that. We can later expand it to iOS and web.
  I: That sounds great, please go ahead.
### Root cause analysis | Spike in Uber ride cancellations
  I: We’re facing a sudden spike in ride cancellations on the Uber app, and customers are getting poor service as a result. Walk me through how you’d find the root cause.
  C?: To start, can you clarify what the app does here and which service the cancellations affect?
  I: The app connects riders with drivers for transport. The issue is ride cancellations.
  C?: One clarification on the metric: are these rider-initiated or driver-initiated cancellations - or both?
  I: Good question - they’re mostly driver-initiated.
  C?: Over what period has this spike been seen?
  I: Recent, mainly the last couple of weeks.
### Root cause analysis | Google Maps ETA discrepancies
  I: Addressing Discrepancies in Google Maps ETA(Just Dial)
  I: You are the PM for Google Maps. Google Maps is showing a shorter ETA than is actually required to travel between two points. Users are reporting that they are arriving at their destination later than expected, even when 
  C?: To better understand the issue, could you provide me with more details about when and where this problem is occurring? | Is there any specific area where users have reported experiencing this problem more frequently? | Is this problem present across all platforms, Android/iOS, Mobile/Web?
  I: Yes, this is present across all platforms and has been only seen in the last couple of days. Additionally, the users are reporting from various regions and routes, so it doesn’t appear to be isolated to a particular area
  C?: Can you confirm if any updates were made to the routing algorithm or the data used for traffic predictions?
  I: The data sources for traffic information remain the same as before. We did roll out a few updates to improve routing algorithm. It’s worth noting that some users have mentioned that the ETA often remains the same regardl
  C?: Could you provide more details about the nature of these updates and how they were expected to improve accuracy?
### Go-to-market | MakeMyTrip enters Dubai
  I: MMT, is considering entering the Dubai market. What should their market entry strategy be?
  I: Yes !
  C?: So, what are MMT's specific objectives and expectations for entering the Dubai market? | Do we have any specific metrics like revenue or profit targets?
  I: The firm's main objective is to maximize its revenue and ROI over the next five years. Dubai's travel market is rapidly growing, driven by increasing tourism and luxury travel. There is no specific revenue target, but th
  C?: What about the competitive landscape? | Who are the key players, and what are their strengths and weaknesses?
  I: The market is competitive with established players like Booking.com and local agencies.
### Product design | LinkedIn for blue-collar workers
  I: Let’s design something like LinkedIn, but for blue-collar workers in India. How would you approach this?
  C?: Before I jump in, can I clarify two small things? | First, are we focusing only on India? | Second, do you want the platform to help with full-time jobs, part-time gigs, or both?
  I: Good questions. Yes, India. And let's include both full-time and part-time work.
  I: Makes sense. How do you understand the users?
  I: Nice. What pain points do you see here?
### Product improvement | Facebook Reactions
  I: Facebook wants to improve its Reactions feature. How would you go about suggesting actions it can take?
  C?: By ‘Reactions’ do we mean the feature where users react to their own or others’ posts via emojis? | Is there a specific user persona to focus on? | And is there a trigger for this - negative feedback, or something else?
  I: You’re right about the feature. There are multiple personas, but restrict yourself to individual users. Assume Facebook wants to drive higher engagement and is exploring how Reactions can help.
  C?: Fair approach?
  I: This seems comprehensive. We can proceed.
  C?: Shall I move to pain points?
  I: Yes, we can proceed.
### Metrics | Instagram creator commerce
  I: You are a product manager at Instagram working on the Creator Commerce product tagging feature. How would you go about measuring its success?
  C?: Is that accurate?
  I: The description is accurate. Please proceed with the rest of the solution.
  I: The approach seems good. Let’s keep the focus on the creators and buyers. You can skip the brand-side metrics for now. Please go on with the journeys.
  I: You’ve captured the journeys accurately. Please go ahead with the metrics.
### Metrics | WhatsApp in-app video playback
  I: How will you measure the success of WhatsApp’s in-app video playing feature?
  I: That sounds good. Please proceed.
  I: Okay, and how would you use these metrics to evaluate the feature’s success?
### Metrics | Success metrics for Gmail
  I: What would be the success metrics for Gmail?
  I: Sure, go ahead
  C?: Should I be focusing on only email feature of the other features should be considered as well?
  I: You can focus only on the mailing feature
  C?: Will that be okay ?
  I: Yes, that is the right approach please proceed
### Strategy | Users moving from WhatsApp to Telegram
  I: How to stop people moving from WhatsApp to Telegram?
  C?: First, What are the primary reasons users are switching to Telegram, unique features Telegram has, and any recent triggers (past 6 months) causing the migration, including trust factors and user experience issues?
  I: Users are switching due to recent updates by Telegram focused on privacy and user control
  C?: What is WhatsApp's main goal in addressing this issue? | Is it user retention, feature parity, or maintaining market dominance?
  I: You are free to decide.
  C?: Is that acceptable?
  I: Sure, please proceed.
### Product design | Podcasts on Spotify
  I: You are a PM at Spotify. You are asked to come with solutions to improve Spotify as a podcast app
  I: That’s correct.
  C?: Are we improving the experience for listeners or creators, or both? | Are we targeting a specific user demographic? | Are there any budget or timeline constraints I should be aware of?
  I: We are focusing only on listeners. For simplicity, assume no specific demographic, budget, or timeline constraints.
  C?: Does that work for you?
  I: Sure, Go ahead.
### Product improvement | BookMyShow engagement
  I: BookMyShow wants to improve engagement and user satisfaction through new experiential features. How would you go about suggesting actions it can take?
  C?: Are we targeting the whole flow from discovery to post-booking, or one phase? | Are we improving engagement across all users, or a priority persona? | And is there a trigger - a drop in repeat usage, or a need for more content creation?
  I: Assume we’re increasing engagement and stickiness across the lifecycle. Focus on individual users who use BookMyShow regularly to book movies and events.
  C?: Sound good?
  I: That works. Go ahead.
  C?: Shall I move to pain points?
  I: Yes, please proceed.
### Product improvement | Improve Hotstar
  I: Can you walk me through how you'd improve the experience of an OTT platform like Hotstar?
  C?: What is the state of our company? | What is the goal of the company at this point?
  I: Let’s assume the company is mature and has a significant urban user base. However, competition is intense, and we want to improve rider experience and increase loyalty.
  C?: Does that sound good?
  I: Sure. Please Go ahead.
  I: That’s quite comprehensive. Can you list down the pain points of these viewers and your solutions?
### Product improvement | Improve YouTube
  I: We would like you to take the lead in improving YouTube. How would you approach this task?
  I: Yes, go ahead
  C?: When you say “Improve Youtube”, is there any specific aspect of “improvement” you’re looking at? | Or are there any areas of user engagement I should focus on?
  I: For the scope of this question, you can choose how you want to define improvement, you can consider any product metric and work towards enhancing it
  I: Sounds good, pleasego ahead.
### Root cause analysis | Prime Video views fall
  I: The video views on Prime Video have gone down. What should we do? (Microsoft)
  C?: What counts as a video view on Prime?
  I: A video is counted as been viewed if at least 70% of the video is watched by the user. Views per day is the metric affected.
  C?: How much has the decline been? | For how long have we seen this issue? | Has the decrease been gradual or sudden?
  I: We have seen a 20% decrease. This has been gradual, over the last month.
  C?: Is this issue prevalent across website and mobile apps on Android and iOS?
  I: Yes, we are noticing this across all platforms, OS versions and devices.
### Pricing | JioSaavn family plan
  I: JioSaavn is a music streaming service that wants to launch a family music plan for its users. How would you go about it?
  I: Yes, go ahead.
  I: Fair enough. How do you go about pricing such a plan?
  I: Okay, go ahead.
### Pricing | JioSaavn family plan (second take)
  I: How would you price the family subscription pack for JioSaavn?
  C?: Am I understanding this correctly?
  I: Yes.
  C?: How many accounts would be present in the family pack?
  I: We would adhere to 5 accounts in a family pack just like others in the industry.
  C?: Do we have a specific goal in mind? | Do we want to wrestle users away from our competitors? | Are we trying to increase our revenue? | Or is there something else we are working on?
  I: We want to increase our market share.
### Pricing | Netflix pricing strategy
  I: The Indian OTT market is intensely competitive and price-sensitive. Netflix has already implemented price cuts and a mobile-only plan. Now, with the global rollout of its 'paid sharing' policy to curb password sharing, y
  I: Yes, that sounds fair. Go ahead.
  I: Sure, you may take your time and go ahead.
  C?: To ground my recommendations in the current market, could you provide the latest pricing tiers for us and our key competitors?
  I: Of course. Here are the current approximate monthly plans: Netflix: Mobile (₹149), Basic (₹199), Standard (₹499), Premium (₹649). Netflix doesn’t offer • annual plans.
### Product design | AI assistant for doctors in small clinics
  I: Designing an AI Assistant to Support Doctors in Small/Medium Clinics
  C?: Is the objective to assist with diagnosis, or mainly to reduce the doctor’s administrative workload?
  I: Focus only on reducing administrative work no diagnosis.
  I: Makes sense. How does that translate to the experience?
  I: Interesting. How would you imagine the assistant working?
### Product improvement | HealthifyMe engagement
  I: HealthifyMe has been seeing low engagement on the app. How would you improve it?
  C?: When did HealthifyMe start seeing this dip in engagement?
  I: By low engagement, I mean users are dropping off very early. Our short-term
  C?: you define as engagement here? | Also, what metrics have been affected?
  I: metrics like onboarding completion and first-week retention have fallen, and churn has increased.
  I: Sure, go ahead.
### Root cause analysis | Duolingo engagement drop
  I: We’re seeing a drop in engagement for Duolingo over the last month. How would you analyse this?
  C?: Correct?
  I: Yes, that’s accurate.
  C?: And as for ‘engagement’, which metric exactly? | DAU/MAU, average session time, or lessons completed per user per week?
  I: For this discussion, engagement is the weekly average number of users who complete at least one lesson. It’s declined about 15% over the past month.
  I: That sounds logical. Please proceed.
### Root cause analysis | Adobe LMS trial-to-paid conversion
  I: Adobe’s LMS product’s free-trial to paid conversion is 4–5% vs. industry benchmark of 7–10%. We want to improve that.
  C?: Is that correct?
  I: Yes.
  C?: What exactly does the product do? | And who typically uses it? | And is this dip in conversion recent or persistent?
  I: It’s an LMS product for internal employee training. It's a subscription offering. Customers are mostly SMBs with average contract size of $50K. Gap has persisted since launch.
  C?: On the competitive landscape, does Adobe’s LMS differ meaningfully from others? | how does a typical customer flow work today? | Free trial →Sales → Customization →Roll-out?
  I: It’s pretty commoditized. Most tools are similar. Yes, that’s the journey. Sales pitches, a technical analyst handles customisations, and then implementation.
### Go-to-market | Launching a social fitness product
  I: Our company wants to launch a social fitness product. How would you develop its go-to-market strategy?
  C?: Product type - Is this a tangible product like a smartwatch, or a smartphone app? | Core value proposition - What does the product do - is it primarily about fitness tracking, social motivation, or a combination? | Third-party integrations - Does the product connect to existing social platforms or wearable devices? | Target market - Who is the intended user, and which geography are we launching in first? | Launch con
  I: It's a smartphone app where users can share workout updates, diet plans, and progress with each other. They can collaborate through in-app video calls and compete in group or individual fitness challenges. The goal is to
### Product design | AI copilot for customer-support agents
  I: Design an AI copilot that helps human agents in a customer-support team. Walk me through your approach.
  C?: Could I clarify a couple of things - who exactly is the copilot for: our own support agents, or end customers directly? | And what channels are we talking about: chat, email, voice?
  I: It’s an internal tool for our own agents. They handle chat and email tickets for a B2B SaaS product - the customer never talks to the copilot directly.
  C?: And what’s the primary outcome the team cares about - faster resolution, higher quality, lower cost, or quicker agent ramp-up?
  I: Cut handling time and improve resolution quality. But a human has to stay accountable for every reply that goes out - we’re not automating the customer away.
  C?: Does that structure work for you?
  I: Yes, that works. Start with the agent.
### Product improvement | Improve Microsoft PowerPoint
  I: You are tasked with improving Microsoft Powerpoint. How will you go about it?
  C?: Toensure we're aligned, could you please clarify what you mean by "improvement"?
  I: By "improvement," we mean enhancing the overall user experience, addressing pain points, and possibly introducing new features that align with user needs and market trends
  C?: Does this overview sound accurate?
  I: Yes, that's a good overview. What would be your next step?
  I: Those personas are well-defined. Which one of these personas would you prioritize?
### Metrics | Measuring an AI email-summary feature
  I: We just shipped an AI feature that auto-summarizes long email threads at the top of our inbox product. How would you measure its success?
  C?: When a user opens a long thread, we show a generated Too Long ; Didn't Read at the top, is that right? | And is the goal mainly to save reading time, or also to drive more replies and actions?
  I: That's right. The main goal is saving reading time and helping users act faster. Trust matters too, we can't have it inventing things.
  C?: Should I start with the product side?
  I: Yes - but before you list metrics, how would you decide where to look?
  I: Good. Go ahead with the product metrics.
### Root cause analysis | Users abandoning an AI chatbot
  I: There is an AI chatbot assistant in our consumer app. Over the last month, users have increasingly been abandoning the conversation mid-way. How would you investigate?
  C?: What exactly do we mean by "abandoning", do you mean users close the chat or users stop responding?
  I: Yes. Users abandon the conversation mid-way without completing the task.
  C?: What is the current abandonment rate, what was the baseline, and did it occur abruptly or gradually?
  I: It's a gradual increase over the last four weeks.
  I: There were no infra incidents recently. However, we have rolled out a new version of the model five weeks back. The latency has been the same.
### Root cause analysis | Low CRM adoption
  I: You're the PM for our CRM's sales module. Usage data shows that only 40% of reps actively use the CRM daily, even though it's mandated by their sales ops team. Leadership wants to know why, and what you'd do about it. Wh
  C?: Is 40% daily login the real problem, or is login healthy but reps aren't updating records once they're in?
  I: Fair question, let me clarify. Login is actually closer to 70%. The 40% refers to reps who log in but don't meaningfully engage: they don't update opportunity stages or log activities, so pipeline data is stale.
  C?: Before I hypothesize on causes, I'd want to segment the 40% who aren't updating: does it cluster by team, region, tenure, or deal size?
  I: Good instinct. It's fairly evenly spread across regions and teams, but it skews toward reps with more than five years of tenure. Newer reps update records far more consistently.
  I: Walk me through each of those.
### Go-to-market | Launching an AI sales assistant
  I: A B2B SaaS company has built an AI Sales Assistant. It joins sales calls, creates meeting summaries, captures action items, and updates CRM fields automatically. The company wants to launch this product for mid-market sa
  C?: Is this a standalone product or an add-on to an existing product?
  I: It is an add-on. The company already sells a CRM workflow tool to mid-market companies.
  C?: Are we trying to drive adoption first, revenue first, or mainly learn from early users?
  I: The immediate goal is adoption among existing customers. Revenue expansion comes next.
  I: What problem would you focus on?
### Product design | Samsung Galaxy Buds experience
  I: You're working at Samsung on the product team for Galaxy Buds. Using listening data, Samsung wants to explore new approaches to improve the listening experience - in particular, how this data might be made social. How wo
  C?: Goal - Is the primary objective improving user engagement, building brand loyalty, or creating monetisation opportunities? | Existing app - Galaxy Buds users already have the Wearable app installed post-purchase - is usage dropping off after setup? | Should we build within it or create something new? | Scope - Are we open to building a standalone social product, or should this live within the existing Samsung ecosyst
  I: Great clarifying questions. Engagement is the priority. You're right that Wearable app usage drops off after setup. We're open to both approaches - I'm interested in what you think makes the most sense from a product sta
  I: Sure. I'm with you on the approach. Please go ahead.
### Product design | Increasing voter turnout
  I: Perugia's voting turnouts have stagnated at 55% in the last few years. The Government of Perugia has hired you to design an application to improve voter turnout. What are some of the features you would recommend for such
  C?: Can I start with a few clarifying questions about the problem?
  I: Sure, go ahead.
  C?: Why has turnout stagnated? | Are the people skipping from a specific demographic? | What are the current voting methods, and is the app meant to be a voting channel itself or only an engagement tool?
  I: Those who skip cite a lack of knowledge of the candidates, low interest in the process, confusion about registration and voting, a sense that their vote doesn't count for much, and being busy on voting day.
  I: The government's awareness campaigns reach only a few. The people skipping are mainly new voters aged 18-30. Voting remains a paper-ballot system and the government doesn't intend to change that. The app should attract m
  C?: May I take a moment to think through the solution?
### Pricing | Pricing an Apple smart speaker
  I: How would you price Apple Home, the smart speaker from Apple?
  C?: Am I correct with this?
  I: Yes, you are correct. One thing I would like to point out – Apple Home can also connect with and control the smart home devices in the house..
  C?: Is Apple Home a new launch by Apple or is it already present in the market?
  I: We are looking to launch Apple Home in the next quarter. We hope to wrestle away at least 20-30% market share from other players in the market
  C?: To come up with the numbers, can you help with the products and prices our competitors Google and Amazon offer?
  I: Sure, let me give you the prices of our competitor products. Google Nest is priced at Rs 7K while Google Nest Mini is priced at Rs 5K. For Alexa, we again have multiple versions ranging from at Rs 5.5K to Rs 10K.
### Go-to-market | Tata Group loyalty programme
  I: The tata group wants to incentivize their customers and want to increase their loyalty towards the brand. We need your help to prepare a loyalty program for the conglomerate.
  I: Yes, that is correct.
  C?: What happens to those?
  I: You can assume that all the existing loyalty programs will be replaced by the new loyalty program that you would suggest.
  I: Good that you mentioned it. In your solution, ensure that there is a smooth transition for the existing reward system.
### Guesstimate | Instagram uploads per day in India
  I: Estimate the number of Instagram uploads occurring in India.
  C?: Should I estimate uploads per day or per year, and should "uploads" include posts, stories, or both?
  C?: Should I consider both personal and business accounts?
  I: Personal accounts only for now.
  C?: Can I assume this estimate is for a typical day, not a festival or a holiday?
  I: You can assume a typical day and start working on your approach.
### Guesstimate | YouTube revenue per day
  I: That sounds good, lets move forward.
  I: Anything else you would like to add?
### Guesstimate | Zoom's daily server usage
  I: Estimate Zoom’s daily server usage
  C?: Shall I proceed with this assumption?
  I: Yes, that sounds reasonable.
  C?: Do you want me to account for global usage or be constrained to a particular geography, such as India?
### Guesstimate | Users of a food-delivery app in South America
  I: Estimate the number of users for a food delivery app in a South American country.
  C?: What is the total population of the country, and should I assume this is a product in its early stage or already launched?
  I: The country has a population of 100 million. You can assume the platform is already launched and is looking to scale. Go ahead with the assumptions you need.
  I: Seems logical. You can proceed with this assumption.
### Guesstimate | Dark stores for 10-minute coverage of Ahmedabad
  I: How many dark stores would a quick-commerce player need in Ahmedabad to guarantee 10- minute delivery across the city?
  C?: Is this the city, or the full district?
  I: City plus immediate suburbs - the area a player would realistically serve.
  C?: A single player, or everyone combined?
  I: A single dominant player, covering the area on its own.
  C?: And does the 10 minutes include pick and pack, or is it pure travel?
  I: Full order-to-doorstep window.
### Guesstimate | WhatsApp chats in India per day
  I: Estimate the number of WhatsApp chats occurring in India in a day?
  C?: We are focusing on chats and not on messages? | Also chats includes individual chats, group chats or both?
  I: Yes, we are focusing on the number of chats and it covers both individual and group chats.
  C?: Is this approach alright?
  I: Sounds like a comprehensive approach, please proceed.
  C?: Does this seem reasonable?
  I: Yes, you may continue.
### Guesstimate | Storage needed by Google Photos
  I: Can you give a quick estimate on how much storage is needed by Google Photos? (Google PM)
  C?: Are we focusing on just photos, or are we considering videos as well?
  I: You can consider only photos.
  C?: Are we considering only clicked photos or we are looking at received photos too?
  C?: Should I consider Gmail users or only Android user?
  I: You can consider only Android.
### Guesstimate | Uber drivers in Bengaluru
  I: Can you quick estimate on how many uber drivers are there in Bangalore? (Samsung R&D)
  C?: Is that correct?
  I: Yes you are right please proceed.
  I: Sounds about right.
  I: Sounds like a fair estimate, go ahead.
### Guesstimate | Google Drive storage for Singapore
  I: Estimate the total storage needed if 200 GB free storage is to be given to people using Google Drive in Singapore
  C?: Are we considering all residents of Singapore or a specific segment like adults or internet users?
  C?: Should we assume that every eligible person will use the full 200 GB of free storage?
  I: You can make reasonable estimates.
  C?: Should we also consider any potential limitations, such as a maximum number of users or an uptake rate?
  I: No specific limitations. Assume maximum possible uptake.
### Guesstimate | Bikes needed for a bike-taxi company
  I: You are starting a bike taxi company, how many bikes would you require? (Google PM)
  C?: Are we starting in a single city or planning to expand to multiple cities simultaneously, like pan-India?
  I: We are just starting out in Bangalore for now.
  I: What other factors will you need to get to a number?
  I: How will you use these factors?
### Guesstimate | Google searches per second
  I: Estimate the number of queries answered by Google per second.
  C?: Is there any particular geography that I should focus on? | And also any particular mode of search like via the mobile or desktop?
  I: You can consider the global population, and both modes of search are acceptable.
  C?: Does that sound fair?
  I: Sure, can you assign some numbers to these factors?
  C?: Is it fair to assume that Google’s market share in search is 90%?
  I: Yes, you can proceed with that.
### Guesstimate | Swiggy orders per hour in India
  I: Can you estimate the number of orders delivered by Swiggy per hour in India?
  C?: Should I consider both peak and off-peak hours in my estimation, or focus on an average over the entire day?”
  I: You can decide.
  C?: Does that sound good?
  I: That is a good approach. Go ahead.
  I: Sure, please proceed.
### Guesstimate | Google Meet calls per day
  I: Estimate the total number of Google meets that happen daily
  I: Yes, go ahead
  C?: Is there any region or country we’re focusing on, or should we look at it globally? | And are we considering only professional meetings or personal as well?
  I: To estimate the total google meets accurately, it would be better if we focus on a global level. Whether to consider professional & personal, that’s a choice you can make
  I: That sounds like a decent logic, please go ahead
### Guesstimate | Users of a Bhojpuri short-movie app
```


## Patterns added during M2 (25 Sep 2026)
- "What changed there, on that date?" for a sudden, local step (Zepto B82: skipped; cancellations B86: asked as "shipped any new feature"). Seen in 2 cases so far; kit unchanged (rule: 3+).
- "From what level to what level?" when a change is given as a bare % (B86). 1 case.
- Goal question asked but left unanswered, and not pushed (A280 GTM, B153 metrics). 2 cases.
- One word hiding two user groups ("vendors": national brands vs local bakeries, A269). 1 case.
- An asset the company already owns (Swiggy Dineout, A280). 1 case.

## Patterns added during M3 (25 Sep 2026)
- "What exists today?" skipped in an AI-feature case (B107: proposed a chatbot Myntra already had a version of). Counts towards card 4 (today and the trigger); kit unchanged.
- "What decision will the metric drive?" skipped in a metrics case (A290), which led to 11 metrics and no priority. 1 case; already a metrics add-on.
- RCA: "exact definition" and "size vs baseline" both skipped (B70), which hid a mix effect (festive category shift). The add-ons exist; a new note for RCA on rates: **ask whether the mix of groups changed**. Seen in 1 case; kit unchanged (rule: 3+).
- Pricing: "new or existing customers?" asked implicitly (A297 split them) but "why now / why the cut?" skipped. 1 case.
- Guesstimates: card 5 (check against a published figure) skipped in B141, done internally in A240 (two paths) but not against real counts. 2 of 2 guesstimates missed an external check. Watch in M4; if it recurs, make the external check its own line on card 5.

## Patterns added during M4 (26 Sep 2026)
- "What exists today?" skipped again: B114 (Maps already has Explore, lists, Ask Maps) and B151 (MakeMyTrip has run a UAE business since ~2014). With B107 (M3) that is **3 cases**. It is already core card 4 (today and the trigger), so no new card; case write-ups now name it as the costliest skip when it happens.
- Design for minors: eligibility and legal limits (state school-vehicle rules) skipped in A250. 1 case; already a design add-on.
- RCA: "size vs baseline" skipped in A306 even in an otherwise excellent opening (did completed trips fall?). With B70 (M3) and B86 (M2) that is 3 cases; the add-on exists; stronger answers now always ask "from what to what, and did the outcome metric move?"
- GTM: "standalone or add-on / right to win" skipped in B151. 1 case.
- Guesstimates: card 5 skipped in both B138 and B140 (now 4 of 4 guesstimates across M3–M4). Rule met: from M4 the card-5 wording names two checks: a per-unit ratio (trips per driver, trips per resident) and, where one exists, a published figure. Also "peak or average?" mattered in B140 (fleet sized on the daily average); card 1 already asks "typical day or peak?".
- Guesstimates: unit ambiguity "bikes owned vs riders on the app" (B140), "registered vs active drivers" (B138). 2 cases.

## Patterns added during M5 (26 Sep 2026)
- "What exists today?" skipped in all three M5 cases: B46 (Apna, WorkIndia, agents, e-Shram), A288 (product tags already live; Live Shopping ended 2023), B149 (3 of 4 proposed WhatsApp features already existed). Now 6 cases across M3–M5. Already core card 4; write-ups name it as the costliest skip each time. No new card.
- Goal skipped in two cases (B46 design, A288 metrics), and in A288 "what decision will the metric drive?" also skipped, which again produced a long unranked list (with A290 in M3: 2 cases).
- Strategy: "what does the key word mean?" (“moving” = uninstalling or starting new groups elsewhere, B149). Sits under card 1 (confirm the thing). 1 case.
- Two-sided design: "who is the hard side, and how dense must it be?" skipped (B46). 1 case (M4 A250 had a similar density gap for vans).
- Guesstimates: card 5 misused in A235 (a published figure was offered by the interviewer but read the wrong way round) and skipped in B136. Now 6 of 6 guesstimates across M3–M5 with a weak or missing check; card 5 already names two checks (per unit, published figure). Card 1: "chat" never defined (B136); unit ambiguity now 3 cases (B138, B140, B136); card 1 already asks for the unit's definition, so the M5 write-ups spell out "define it so it can't be misread".

## Patterns added during M6 (27 Sep 2026)
- "What exists today?" skipped again in all three M6 cases: B105 (character lookup exists as Prime Video X-Ray), B80 (Prime Video already rents single films and runs a free, ad-supported app), A299 (Netflix never offered a paid extra member in India). Now 9 cases across M3–M6. Already core card 4; no new card. In A299 it decided the whole recommendation.
- "Today and the trigger" as timing: B105 never asked *when* loyalty drops (the post-IPL cliff). Counts under card 4.
- RCA: "is the data trustworthy / has counting changed?" skipped in B80 despite a model opening (definition, size, timing, platform, region all asked). With A308 (M1) that is 2 cases. New RCA habit in write-ups: **split the metric into its parts** (views = viewers × starts × finish rate) before external checks. 1 case so far; kit unchanged (rule: 3+).
- Pricing: "plan structure" skipped (A299), and existing customers who might trade down never counted. 1 case.
- Guesstimates: card 5 misread in A236 (a US share of a quarter to a third should have raised a flag) and skipped in B144. Now 8 of 8 guesstimates across M3–M6 with a weak or missing check. Card 1 unit ambiguity again in B144 (“potential users”: triers vs monthly users): 4 cases; card 1 wording already asks for the definition.

## Patterns added during M7 (27 Sep 2026)
- "What exists today?" skipped again: B50 (ABHA-linked records and Scan and Share already move lab reports; clinic software exists), A303 (Duolingo already shows a "Can't speak now" button). B97 listed existing features but missed that Google Fit APIs close at the end of 2026. Now 11–12 cases across M3–M7. Already core card 4; no new card.
- Design: legal and safety edges skipped in B50 ("no diagnosis" treated as a scope note, not a design rule; DPDP consent for health data; patient language). Design add-on "eligibility or legal limits" already covers it (with A250 in M4: 2 cases).
- Improvement: the interviewer offered data (two falling metrics) and the candidate used personal experience instead (B97). New habit in write-ups: ask for the funnel before naming the pain. 1 case.
- RCA: "is the data trustworthy / has counting changed?" skipped in A303. With A308 (M1) and B80 (M6) that is **3 cases**; it is already an RCA add-on, so no kit change, but stronger RCA answers now always ask it.
- RCA: "scope of the metric" (worldwide or one market?) skipped in A303, and it decided whether the found cause could explain the whole drop. New habit "check the cause adds up to the whole fall". 1 case.
- Guesstimates: card 1 unit errors in both A237 (data counted one direction only) and B143 (joins counted as meetings). Unit ambiguity now 6 cases across M3–M7; card 1 already says "pin down the unit", and M7's reminder adds the key idea "count the right unit". Card 5 skipped in both: 10 of 10 guesstimates with a weak or missing check.

## Patterns added during M8 (27 Sep 2026)
- "What exists today?" skipped again in two of three M8 cases: A267 (Freshdesk, Zendesk, Intercom and Salesforce already sell support copilots; buy vs build is the first decision), A283 (reps already use free AI note-takers; rivals Gong, Salesforce and Zoho AI never named). Now 13–14 cases across M3–M8. Already core card 4; no new card.
- "Today and the trigger" as volume: A267 never asked tickets a day, handle time or why now, so the prize was never sized. Counts under card 4.
- Edges: A283 never asked about languages or phone vs video calls; in India most field-sales calls happen on mobiles and WhatsApp, where a meeting bot can't join. Edges are core card 5; 1 case where it decided the target segment.
- RCA: A311 asked the exact definition, segmented, and checked data trust (duplicates) but skipped "since when / recent changes". Already an RCA add-on.
- B2B pattern: "who is the buyer, who is the user, and what does each get?" named in A283 but missed in A311, where it was the root cause. 2 cases; covered by the M8 framework box, not a kit card (rule: 3+).
- Pricing inside GTM: "cost to serve one use" skipped in A283 (per-user price for an AI product with per-call-hour costs). With A299's plan-structure skip (M6), pricing add-ons already cover it ("cost floor").
- Guesstimates: card 4 errors in both B137 (file sizes swapped between clicked and received photos, ~2.4× too big) and B139 (60% average use of a free quota, ~7× too high); card 1 unit error in B139 (data stored vs disk needed). Card 5 skipped in both: 12 of 12 guesstimates with a weak or missing check. M8's reminder adds the key idea "stored is not the same as offered".

## Patterns added during M9 (27 Sep 2026)
- Today and the trigger: A285 designed a Tata loyalty programme from scratch though Tata Neu and NeuCoins have run since 2022; A245 never asked what the government already offers (ECI's Voter Helpline app exists in India). "What exists today?" now skipped in 15–16 of the cases read; already core card 4. No kit change.
- Goal: B93 accepted "20–30% share" alongside a premium price without asking which wins; the speaker needs an iPhone, so the reachable market is iPhone homes. Goal conflicts (share vs profit) now in 3 pricing cases across M3, M6, M9; already a pricing add-on ("share or profit?"). No kit change.
- Who: B93 missed that only iPhone owners can buy; "who can actually buy or use it?" 2 cases (B93, plus the Galaxy-only Wearable app in A264). Below the 3-case rule.
- Design: A245 used "users vs non-users" as its North Star (selection bias); holdout needed. Measurement-bias pattern now in 3 cases across M1 (Google Pay), M7, M9, but it belongs to the answer's measure step, not the opening kit. No kit change.
- Guesstimates: card 1 (unit) skipped in both (A239 "users" undefined; B142 asked peak vs average, then divided by 24). Unit errors now in 8 guesstimates; card 1 already names it. Card 5 (check) skipped in both, 14 of 14 across M3–M9.
